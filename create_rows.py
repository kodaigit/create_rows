from row_placement import create_scene_with_rows


# Edit these paths and parameters for your scene.
SCENE_FILE = "/home/kodai/mavs_latest/data/scenes/aai_field.json"
MESH_DIR = "/home/kodai/mavs_latest/data/scenes/meshes/cotton/objective1_related/colmapOpenMVS" #this is folder where the script searches for obj files
MESHES_ROOT = "/home/kodai/mavs_latest/data/scenes/meshes" #this is path to the "meshes" folder of MAVS
OUTPUT_FILE = "/home/kodai/mavs_latest/data/scenes/test_fucntion.json"

FIRST_ROW_START = [-43.457, 167.19]
FIRST_ROW_END = [-54.948, 49.131]

PLANT_SPACING = 1
ROW_SPACING = 1
NUM_ROWS = 100
ROW_SIDE = 1  # Flip between 1 and -1 if rows are generated on the wrong side of the first row.

SCALE = [1.0, 1.0, 1.0] #scale is the same for all meshes in rows 
Z_VALUE = 0.0 # z value of position of all meshes added 
POSITION_NOISE_STD = 0.01 # noise is sample from gaussian mean of 0 and this STD
LABEL_BY_GROUP = True #if u want to turn on labling for meshes added, set True. 
SEED = 7 #used for functions involving randomness (mesh selection, mesh x,y location noise, and mesh orientation noise)


def main():
    create_scene_with_rows(
        scene_file=SCENE_FILE,
        mesh_dir=MESH_DIR,
        output_file=OUTPUT_FILE,
        first_row_start=FIRST_ROW_START,
        first_row_end=FIRST_ROW_END,
        plant_spacing=PLANT_SPACING,
        row_spacing=ROW_SPACING,
        num_rows=NUM_ROWS,
        scale=SCALE,
        meshes_root=MESHES_ROOT,
        row_side=ROW_SIDE,
        position_noise_std=POSITION_NOISE_STD,
        z_value=Z_VALUE,
        label_by_group=LABEL_BY_GROUP,
        seed=SEED,
    )
    print(f"Scene with rows written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
