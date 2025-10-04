#!/usr/bin/env python3
"""
Visualizaciones Ejecutivas para Análisis de Siniestros Viales CABA
Diseñadas para presentaciones de alto nivel ante Secretarías de Movilidad
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import folium
from folium.plugins import HeatMap
import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo profesional
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Colores corporativos para presentaciones ejecutivas
COLORS = {
    'primary': '#1f77b4',
    'secondary': '#ff7f0e', 
    'accent': '#2ca02c',
    'danger': '#d62728',
    'warning': '#ff9800',
    'success': '#4caf50',
    'info': '#2196f3'
}

def load_and_prepare_data():
    """
    Carga y prepara los datos para análisis
    """
    try:
        # Cargar datos desde Excel - usar solo la hoja HECHOS que ya tiene toda la info
        df = pd.read_excel('homicidios.xlsx', sheet_name='HECHOS')
        
        # Limpiar y preparar datos
        df['FECHA'] = pd.to_datetime(df['FECHA'])
        df['AÑO'] = df['FECHA'].dt.year
        df['MES'] = df['FECHA'].dt.month
        df['DIA_SEMANA'] = df['FECHA'].dt.day_name()
        df['HORA_NUM'] = pd.to_numeric(df['HH'], errors='coerce')
        
        # Cargar también datos de víctimas para análisis más completo
        try:
            df_victimas = pd.read_excel('homicidios.xlsx', sheet_name='VICTIMAS')
            # Fusionar con datos de víctimas si es posible
            df = pd.merge(df, df_victimas, on='ID', how='left', suffixes=('', '_victima'))
        except:
            print("Nota: No se pudieron cargar datos adicionales de víctimas")
        
        return df
    except Exception as e:
        print(f"Error cargando datos: {e}")
        return None

def create_executive_summary_chart(df):
    """
    Crea un gráfico de resumen ejecutivo con KPIs principales
    """
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Evolución Temporal', 'Distribución por Tipo de Víctima', 
                       'Hotspots por Comuna', 'Patrón Horario'),
        specs=[[{"secondary_y": True}, {"type": "pie"}],
               [{"type": "bar"}, {"type": "scatter"}]]
    )
    
    # 1. Evolución temporal
    yearly_data = df.groupby('AÑO').size()
    fig.add_trace(
        go.Scatter(x=yearly_data.index, y=yearly_data.values, 
                  mode='lines+markers', name='Siniestros por Año',
                  line=dict(color=COLORS['primary'], width=3)),
        row=1, col=1
    )
    
    # 2. Distribución por tipo de víctima
    victim_types = df['VICTIMA'].value_counts().head(5)
    fig.add_trace(
        go.Pie(labels=victim_types.index, values=victim_types.values,
               name="Tipo de Víctima", hole=0.3),
        row=1, col=2
    )
    
    # 3. Hotspots por comuna
    comuna_data = df.groupby('COMUNA').size().sort_values(ascending=True).tail(10)
    fig.add_trace(
        go.Bar(x=comuna_data.values, y=comuna_data.index,
               orientation='h', name='Siniestros por Comuna',
               marker_color=COLORS['danger']),
        row=2, col=1
    )
    
    # 4. Patrón horario
    hourly_data = df.groupby('HORA_NUM').size()
    fig.add_trace(
        go.Scatter(x=hourly_data.index, y=hourly_data.values,
                  mode='lines+markers', name='Patrón Horario',
                  line=dict(color=COLORS['accent'], width=2)),
        row=2, col=2
    )
    
    fig.update_layout(
        title_text="Dashboard Ejecutivo - Siniestros Viales CABA",
        title_x=0.5,
        title_font_size=20,
        height=800,
        showlegend=False,
        template="plotly_white"
    )
    
    fig.write_html("dashboard_ejecutivo.html")
    fig.write_image("dashboard_ejecutivo.png", width=1200, height=800, scale=2)
    
    return fig

def create_heatmap_temporal(df):
    """
    Crea un mapa de calor temporal elegante
    """
    # Crear matriz de datos por día de semana y hora
    df_pivot = df.pivot_table(
        values='ID', 
        index='DIA_SEMANA', 
        columns='HORA_NUM', 
        aggfunc='count', 
        fill_value=0
    )
    
    # Reordenar días de la semana
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    df_pivot = df_pivot.reindex(days_order)
    
    plt.figure(figsize=(16, 8))
    sns.heatmap(df_pivot, 
                cmap='YlOrRd', 
                annot=False, 
                fmt='d',
                cbar_kws={'label': 'Número de Siniestros'},
                linewidths=0.5)
    
    plt.title('Patrón Temporal de Siniestros Viales - CABA\n(Análisis por Día de Semana y Hora)', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Hora del Día', fontsize=12)
    plt.ylabel('Día de la Semana', fontsize=12)
    plt.xticks(rotation=0)
    plt.yticks(rotation=0)
    plt.tight_layout()
    
    plt.savefig('heatmap_temporal.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_geospatial_analysis(df):
    """
    Crea análisis geoespacial avanzado
    """
    # Filtrar datos con coordenadas válidas
    df_geo = df.dropna(subset=['pos x', 'pos y'])
    
    if len(df_geo) == 0:
        print("No hay datos geoespaciales válidos")
        return None
    
    # Crear mapa base centrado en CABA
    center_lat = df_geo['pos y'].mean()
    center_lon = df_geo['pos x'].mean()
    
    m = folium.Map(
        location=[center_lat, center_lon],
        zoom_start=11,
        tiles='CartoDB positron'
    )
    
    # Agregar mapa de calor
    heat_data = [[row['pos y'], row['pos x']] for idx, row in df_geo.iterrows()]
    HeatMap(heat_data, radius=15, blur=10, max_zoom=1).add_to(m)
    
    # Agregar marcadores para puntos críticos
    hotspots = df_geo.groupby(['pos x', 'pos y']).size().reset_index(name='count')
    hotspots = hotspots.nlargest(10, 'count')
    
    for idx, row in hotspots.iterrows():
        folium.CircleMarker(
            location=[row['pos y'], row['pos x']],
            radius=row['count'],
            popup=f"Siniestros: {row['count']}",
            color='red',
            fill=True,
            fillColor='red',
            fillOpacity=0.7
        ).add_to(m)
    
    m.save('mapa_hotspots_ejecutivo.html')
    return m

def create_predictive_insights(df):
    """
    Crea visualizaciones de insights predictivos
    """
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    
    # 1. Tendencia por año con proyección
    yearly_data = df.groupby('AÑO').size()
    axes[0,0].plot(yearly_data.index, yearly_data.values, 'o-', linewidth=3, markersize=8)
    
    # Agregar línea de tendencia
    z = np.polyfit(yearly_data.index, yearly_data.values, 1)
    p = np.poly1d(z)
    future_years = np.arange(2022, 2025)
    axes[0,0].plot(np.concatenate([yearly_data.index, future_years]), 
                   p(np.concatenate([yearly_data.index, future_years])), 
                   '--', alpha=0.7, color='red', label='Proyección')
    
    axes[0,0].set_title('Evolución y Proyección de Siniestros', fontsize=14, fontweight='bold')
    axes[0,0].set_xlabel('Año')
    axes[0,0].set_ylabel('Número de Siniestros')
    axes[0,0].legend()
    axes[0,0].grid(True, alpha=0.3)
    
    # 2. Análisis por tipo de vehículo
    vehicle_data = df['ACUSADO'].value_counts().head(8)
    axes[0,1].barh(vehicle_data.index, vehicle_data.values, color=sns.color_palette("viridis", len(vehicle_data)))
    axes[0,1].set_title('Vehículos Involucrados en Siniestros', fontsize=14, fontweight='bold')
    axes[0,1].set_xlabel('Número de Casos')
    
    # 3. Distribución por edad de víctimas
    age_data = df['EDAD'].dropna()
    axes[1,0].hist(age_data, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
    axes[1,0].axvline(age_data.mean(), color='red', linestyle='--', linewidth=2, label=f'Media: {age_data.mean():.1f} años')
    axes[1,0].set_title('Distribución de Edad de las Víctimas', fontsize=14, fontweight='bold')
    axes[1,0].set_xlabel('Edad')
    axes[1,0].set_ylabel('Frecuencia')
    axes[1,0].legend()
    axes[1,0].grid(True, alpha=0.3)
    
    # 4. Análisis por género
    gender_data = df['SEXO'].value_counts()
    colors = ['lightcoral', 'lightblue']
    wedges, texts, autotexts = axes[1,1].pie(gender_data.values, labels=gender_data.index, 
                                            autopct='%1.1f%%', colors=colors, startangle=90)
    axes[1,1].set_title('Distribución por Género', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('insights_predictivos.png', dpi=300, bbox_inches='tight')
    plt.show()

def create_kpi_dashboard(df):
    """
    Crea un dashboard de KPIs ejecutivos
    """
    # Calcular KPIs principales
    total_siniestros = len(df)
    total_victimas = df['N_VICTIMAS'].sum()
    tasa_mortalidad = (total_victimas / 3000000) * 100000  # Por 100k habitantes
    
    # Crear figura con métricas
    fig = go.Figure()
    
    # Agregar indicadores
    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = total_siniestros,
        delta = {"reference": 800, "valueformat": ".0f"},
        title = {"text": "Total Siniestros<br><span style='font-size:0.8em;color:gray'>2016-2021</span>"},
        domain = {'x': [0, 0.33], 'y': [0.7, 1]}
    ))
    
    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = total_victimas,
        delta = {"reference": 850, "valueformat": ".0f"},
        title = {"text": "Total Víctimas<br><span style='font-size:0.8em;color:gray'>Fatales</span>"},
        domain = {'x': [0.33, 0.66], 'y': [0.7, 1]}
    ))
    
    fig.add_trace(go.Indicator(
        mode = "number+delta",
        value = tasa_mortalidad,
        delta = {"reference": 15, "valueformat": ".1f"},
        title = {"text": "Tasa Mortalidad<br><span style='font-size:0.8em;color:gray'>Por 100k hab</span>"},
        domain = {'x': [0.66, 1], 'y': [0.7, 1]}
    ))
    
    # Agregar gráfico de tendencia mensual
    monthly_data = df.groupby([df['FECHA'].dt.year, df['FECHA'].dt.month]).size().reset_index()
    monthly_data['fecha'] = pd.to_datetime(monthly_data[['FECHA', 'level_1']].rename(columns={'level_1': 'month'}))
    
    fig.add_trace(go.Scatter(
        x=monthly_data['fecha'],
        y=monthly_data[0],
        mode='lines+markers',
        name='Tendencia Mensual',
        line=dict(color=COLORS['primary'], width=2),
        yaxis='y2'
    ))
    
    fig.update_layout(
        title="KPIs Ejecutivos - Seguridad Vial CABA",
        title_x=0.5,
        height=600,
        template="plotly_white",
        yaxis2=dict(
            title="Siniestros por Mes",
            overlaying="y",
            side="right",
            domain=[0, 0.6]
        )
    )
    
    fig.write_html("kpi_dashboard.html")
    fig.write_image("kpi_dashboard.png", width=1200, height=600, scale=2)
    
    return fig

def main():
    """
    Función principal para generar todas las visualizaciones
    """
    print("🚀 Generando Visualizaciones Ejecutivas para Siniestros Viales CABA")
    print("=" * 70)
    
    # Cargar datos
    print("📊 Cargando y preparando datos...")
    df = load_and_prepare_data()
    
    if df is None:
        print("❌ Error: No se pudieron cargar los datos")
        return
    
    print(f"✅ Datos cargados: {len(df)} registros")
    
    # Generar visualizaciones
    print("\n📈 Generando Dashboard Ejecutivo...")
    create_executive_summary_chart(df)
    
    print("🔥 Generando Mapa de Calor Temporal...")
    create_heatmap_temporal(df)
    
    print("🗺️ Generando Análisis Geoespacial...")
    create_geospatial_analysis(df)
    
    print("🔮 Generando Insights Predictivos...")
    create_predictive_insights(df)
    
    print("📊 Generando Dashboard de KPIs...")
    create_kpi_dashboard(df)
    
    print("\n🎉 ¡Visualizaciones ejecutivas generadas exitosamente!")
    print("📁 Archivos creados:")
    print("   - dashboard_ejecutivo.html/png")
    print("   - heatmap_temporal.png")
    print("   - mapa_hotspots_ejecutivo.html")
    print("   - insights_predictivos.png")
    print("   - kpi_dashboard.html/png")

if __name__ == "__main__":
    main()
