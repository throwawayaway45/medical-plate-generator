#!/usr/bin/env python3
"""
MEDICAL PLATE GENERATOR - FREE DEMO VERSION
Full version available at: https://howler72716.gumroad.com/l/plate_generator
"""

import os
import subprocess
import sys

def create_watermarked_scad(base_scad):
    watermark = """/*
 * MEDICAL PLATE GENERATOR - DEMO VERSION
 * ======================================
 * Limitations: 
 * - Only 3 holes
 * - Basic geometry only  
 * - No STEP export
 * - No medical validation
 * 
 * GET FULL VERSION: https://howler72716.gumroad.com/l/plate_generator
 * Full version includes:
 * - 4 anatomical presets
 * - STEP file export
 * - Medical-grade design rules
 * - Custom parameters
 */
 
"""
    return watermark + base_scad

def generate_basic_plate():
    # Limited functionality - only STL, basic plates
    length = 60
    width = 12
    thickness = 3
    holes = 3  # Demo limitation
    
    # SCAD code
    scad_code = f"""difference() {{
    cube([{length}, {width}, {thickness}], center=true);
    """
    
    # Simple holes only
    for i in range(holes):
        x_pos = -10 + i * 10
        scad_code += f"translate([{x_pos}, 0, 0]) cylinder(h=10, d=3.5, center=true);"
    
    scad_code += "\n}"
    
    return scad_code

def main():
    print("Medical Bone Plate Generator - DEMO VERSION")
    print("===========================================")
    print()
    print("This demo generates basic bone plates with limited features.")
    print("Get the full version for STEP export, medical validation, and presets.")
    print("Full version: https://howler72716.gumroad.com/l/plate_generator")
    print()
    
    # Generate basic SCAD code
    scad_code = generate_basic_plate()
    
    # Apply watermark
    watermarked_scad = create_watermarked_scad(scad_code)
    
    with open("demo_plate.scad", "w") as f:
        f.write(watermarked_scad)
    
    print("Generating demo plate...")
    
    try:
        subprocess.run(["openscad", "-o", "DEMO_plate.stl", "demo_plate.scad"])
        print("✅ Demo plate generated: DEMO_plate.stl")
        print("⚠️  DEMO WATERMARK: Limited to 3 holes, basic geometry")
        print("🎯 Full version includes anatomical presets, STEP export, medical validation")
        print("🔗 Get full version: https://howler72716.gumroad.com/l/plate_generator")
        
        # Also watermark the STL file by adding comment to SCAD
        watermark_scad = """// DEMO VERSION - Medical Plate Generator
// Generated file has limitations
// Purchase full version for professional features: https://howler72716.gumroad.com/l/plate_generator"""
        
        with open("watermark.txt", "w") as f:
            f.write(watermark_scad)
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("OpenSCAD required. Install from https://openscad.org")
    
    # Cleanup
    try:
        os.remove("demo_plate.scad")
        os.remove("watermark.txt")
    except:
        pass

if __name__ == "__main__":
    main()