import os
import sys
import subprocess
import shutil

if len(sys.argv) < 2:
  print 'please specify node version'
  sys.exit()

version = sys.argv[1]
platform = subprocess.check_output('node --eval "process.stdout.write(process.platform)"', shell=True);
arch = subprocess.check_output('node --eval "process.stdout.write(process.arch)"', shell=True);

print 'precompiling for ' + platform + '/' + arch + '...'

# patch node-gyp, while --target does not work: lib/configure.js: versionStr = process.env['NODEGYP_TARGET'] || process.version; 
os.putenv('NODEGYP_TARGET', version) 
os.system('node-gyp rebuild')

out_file = os.path.join('build', 'Release', 'nodetime_native.node')
if os.path.exists(out_file):
  target_path = os.path.join('..', 'nodetime', 'compiled', platform, arch, version)
  if not os.path.isdir(target_path):
     os.makedirs(target_path)
  shutil.copy(out_file, target_path)

