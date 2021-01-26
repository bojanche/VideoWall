import ffmpeg
import threading
import sys


#
try:
    in_stream = ffmpeg.probe('./tmp_storage/pitch.mp4')
except ffmpeg.Error as e:
    print(e.stderr, file=sys.stderr)
    sys.exit(1)


video_stream = next((stream for stream in in_stream['streams'] if stream['codec_type'] == 'video'), None)
if video_stream is None:
    print('No video stream found', file=sys.stderr)
    sys.exit(1)

in_stream = ffmpeg.input('./tmp_storage/pitch.mp4')

### High stream
out_stream_high = ffmpeg.output(in_stream, './tmp_storage/high/pitch.m3u8', format='hls', start_number=0,
                                hls_time=6, hls_list_size=0, vcodec='libx265', crf=26, **{'qscale:v': 3})
high = threading.Thread(target=ffmpeg.run, args=(out_stream_high,))
high.start()
### End High Stream

# Testing for file reduction size

### Low Stream
out_stream_low = ffmpeg.filter(in_stream, filter_name='scale', size='640x320').output(in_stream, './tmp_storage/low/pitch.m3u8', format='hls', start_number=0, hls_time=10,
                           hls_list_size=0, vcodec='libx265', crf=27, **{'qscale:v': 3})
low = threading.Thread(target=ffmpeg.run, args=(out_stream_low, ))
low.start()
### End Low Stream

# ffmpeg.run(out_stream_high)
# ffmpeg.run(out_stream_low)
# 640x360