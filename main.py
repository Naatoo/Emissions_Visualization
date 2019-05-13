from csv_parser import CSVFileParser
from interpolator import Interpolator
from interactive_map import InteractiveMap


def create_csv_json_files() -> None:
    parser = CSVFileParser(source_file_name,  **{"country": country_code})
    interpolator = Interpolator(target_file_name, parser.data, parser.coordinates, boundary_values=boundaries)
    interpolator.interpolate(zoom_value=zoom_value, order=order)


if __name__ == "__main__":

    source_file_name = "PM10_raw.txt"
    target_file_name = "PM10_zoomed"
    country_code = "PL"
    zoom_value = 2
    order = 5
    boundaries = {
        "lat_min": 18.55,
        "lat_max": 22.05,
        "lon_min": 49.55,
        "lon_max": 53.05
    }
    create_csv_json_files()

    layer_name = "Data zoomed x{}".format(str(zoom_value))
    fill_color = "Oranges"
    fill_opacity = 0.7
    line_opacity = 0

    inter_map = InteractiveMap(target_file_name, layer_name, fill_color, fill_opacity, line_opacity)
    inter_map.write_to_file()
    inter_map.run_map_and_freeze()