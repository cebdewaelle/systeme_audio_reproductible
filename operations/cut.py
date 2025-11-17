from pydub import AudioSegment
import os


def sar_cut(source_file, position, output_file):
    source_file = os.path.join("audio", source_file)
    output_file = os.path.join("audio", output_file)

    first_sound = AudioSegment.from_file(source_file)

    before_cut = first_sound[:position]

    before_cut.export(output_file, format="mp3")
