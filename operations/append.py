from pydub import AudioSegment
import os


def sar_append(source_file, file_to_append, output_file):

    source_file = os.path.join("audio", source_file)
    file_to_append = os.path.join("audio", file_to_append)
    output_file = os.path.join("audio", output_file)

    first_sound = AudioSegment.from_file(source_file)
    second_sound = AudioSegment.from_file(file_to_append)

    combined = first_sound.append(second_sound)

    combined.export(output_file, format="mp3")
