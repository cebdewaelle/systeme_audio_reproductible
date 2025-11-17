from pydub import AudioSegment
import os

def sar_fade(source_file, fade_in_position, fade_out_position, effect_duration, output_file):
    input_sound = os.path.join("audio", source_file)
    output_file = os.path.join("audio", output_file)

    source = AudioSegment.from_file(input_sound)

    faded_sound = source.fade(to_gain=-30, start=fade_in_position, duration=effect_duration)

    faded_sound_2 = faded_sound.fade(to_gain=30, start=fade_out_position, duration=effect_duration)

    # momentum = position

    # first_thirty_seconds = source[:momentum]

    # silence = source[:30000] -50

    # faded_sound = first_thirty_seconds.append(silence, crossfade=1000)

    faded_sound_2.export(output_file, format="mp3")
    return output_file