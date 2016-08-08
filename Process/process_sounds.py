import os
from header_common import *
from module_info import *
from module_sounds import *

# http://stackoverflow.com/a/8462613
def _path_insensitive(path):
    """
    Recursive part of path_insensitive to do the work.
    """

    if path == '' or os.path.exists(path):
        return path

    base = os.path.basename(path)  # may be a directory or a file
    dirname = os.path.dirname(path)

    suffix = ''
    if not base:  # dir ends with a slash?
        if len(dirname) < len(path):
            suffix = path[:len(path) - len(dirname)]

        base = os.path.basename(dirname)
        dirname = os.path.dirname(dirname)

    if not os.path.exists(dirname):
        dirname = _path_insensitive(dirname)
        if not dirname:
            return

    # at this point, the directory exists but not the file

    try:  # we are expecting dirname to be a directory, but it could be a file
        files = os.listdir(dirname)
    except OSError:
        return

    baselow = base.lower()
    try:
        basefinal = next(fl for fl in files if fl.lower() == baselow)
    except StopIteration:
        return

    if basefinal:
        return os.path.join(dirname, basefinal) + suffix
    else:
        return

def write_python_header(sounds):
  file = open("./IDs/ID_sounds.py","w")
  for i_sound in xrange(len(sounds)):
    file.write("snd_%s = %d\n"%(sounds[i_sound][0],i_sound))
  file.write("\n\n")
  file.close()

def write_sounds(sound_samples, sounds):
  ofile = open(export_dir + "sounds.txt","w")
  ofile.write("soundsfile version 2\n")
  ofile.write("%d\n"%len(sound_samples))
  for sound_sample in sound_samples:
    ofile.write(" %s %d\n"%sound_sample)
  ofile.write("%d\n"%len(sounds))
  for sound in sounds:
    ofile.write("snd_%s %d %d "%(sound[0], sound[1],len(sound[2])))
    sample_list = sound[2]
    for s in  sample_list:
      ofile.write("%d "%(s))
    ofile.write("\n")
  ofile.close()

def compile_sounds(sounds):
  all_sounds = []
  for sound in sounds:
    sound_files = sound[2]
    sound_flags = sound[1]
    for i_sound_file in xrange(len(sound_files)):
      sound_file = sound_files[i_sound_file]
      print(os.path.isfile(export_dir + "Sounds/" + sound_file), _path_insensitive(export_dir + "Sounds/" + sound_file) != None, sound_file)
      if not os.path.isfile(export_dir + "Sounds/" + sound_file) and _path_insensitive(export_dir + "Sounds/" + sound_file) != None:
        print("%s not found in the mod, check case sensitivity." % sound_file)
      sound_no = 0
      found = 0
      while (sound_no< (len(all_sounds))) and (not found):
        if all_sounds[sound_no][0] == sound_file:
          found = 1
        else:
          sound_no += 1
      if not found:
        all_sounds.append((sound_file,sound_flags))
        sound_no = len(all_sounds) - 1
      sound_files[i_sound_file] = sound_no
  return all_sounds

print "Exporting sounds..."
sound_samples = compile_sounds(sounds)
write_sounds(sound_samples, sounds)
write_python_header(sounds)
