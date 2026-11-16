"""Gjør en PNG-illustrasjon om til SVG og en 480 px PNG.

Bruk:  python3 verktoy/vektoriser.py inn.png assets/illustrasjoner/<navn>
Krever: pip install vtracer cairosvg
"""
import sys, vtracer, cairosvg
inn, ut = sys.argv[1], sys.argv[2]
vtracer.convert_image_to_svg_py(inn, ut + ".svg", colormode="color", hierarchical="stacked", mode="spline",
    filter_speckle=6, color_precision=6, layer_difference=18, corner_threshold=60,
    length_threshold=4.0, max_iterations=10, splice_threshold=45, path_precision=2)
cairosvg.svg2png(url=ut + ".svg", write_to=ut + ".png", output_width=480, output_height=480)
print("Lagret", ut + ".svg og", ut + ".png")
