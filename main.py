from FFmeg import ffmpeg_module

ffmpOper = ffmpeg_module()

operation = input("Provide input for operations to be perfomed with spaces "
                  "\n1. Trimming"
                  "\n2. Change aspect ratio"
                  "\n3. Change Bitrate"
                  "\n4. Change frame rate"
                  "\n5. Change frame size"
                  "\n6. Mute Audio"
                  "\n7. Remove Video"
                  "\n8. Convert MP4 to HLS\n")

operation = operation.split(" ")
ffmpOper.copy_file()

if('1' in operation):
    trim_start = input("Enter the start time for trimming eg. 10.00")
    trim_stop = input("Enter the stop time for trimming eg. 10.00")
    ffmpOper.trimming(startduration=trim_start, endduration=trim_stop)

if('2' in operation):
    aspect_ratio = input("Enter the aspect ratio eg ")
    ffmpOper.change_aspect_ratio(aspectratio=aspect_ratio)

if('3' in operation):
    bit_rate = input("Enter the value of bitrate")
    ffmpOper.change_bitrate(BitRateValue=bit_rate)

if('4' in operation):
    frame_rate = input("Enter the frame rate in fps")
    ffmpOper.change_frame_rate(framerate=frame_rate)

if('5' in operation):
    frame_size = input("Enter the frame size you want to keep")
    ffmpOper.change_frame_size(framesize=frame_size)

if('6' in operation):
    ffmpOper.mute_audio()


if('7' in operation):
    ffmpOper.remove_video()


if('8' in operation):
    ffmpOper.convert_hls()


print("Video has been modified")