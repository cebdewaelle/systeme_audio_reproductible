from pydub import AudioSegment
import os


def sar_overlay(source_file1, source_file2, output_file, position, gain_during_overlay):

    source_file1 = os.path.join("audio", source_file1)
    source_file2 = os.path.join("audio", source_file2)
    output_file = os.path.join("audio", output_file)

    source1 = AudioSegment.from_file(source_file1)
    source2 = AudioSegment.from_file(source_file2)

    played_together = source1.overlay(source2, position)

    played_together.export(output_file, format="mp3")
    return output_file
