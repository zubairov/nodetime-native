import os
import sys
import subprocess
import shutil


versions = [
  'v0.6.0',
  'v0.6.1',
  'v0.6.10',
  'v0.6.11',
  'v0.6.12',
  'v0.6.13',
  'v0.6.14',
  'v0.6.15',
  'v0.6.16',
  'v0.6.17',
  'v0.6.18',
  'v0.6.19',
  'v0.6.2',
  'v0.6.20',
  'v0.6.21',
  'v0.6.3',
  'v0.6.4',
  'v0.6.5',
  'v0.6.6',
  'v0.6.7',
  'v0.6.8',
  'v0.6.9',
  'v0.8.0',
  'v0.8.1',
  'v0.8.10',
  'v0.8.11',
  'v0.8.12',
  'v0.8.13',
  'v0.8.14',
  'v0.8.15',
  'v0.8.16',
  'v0.8.17',
  'v0.8.18',
  'v0.8.19',
  'v0.8.2',
  'v0.8.20',
  'v0.8.21',
  'v0.8.22',
  'v0.8.3',
  'v0.8.4',
  'v0.8.5',
  'v0.8.6',
  'v0.8.7',
  'v0.8.8',
  'v0.8.9',
  'v0.10.0',
  'v0.10.1'
]


if len(sys.argv) > 1:
  # for each new version: 1) install nodejs; 2) install node-gyp;
  versions = [sys.argv[1]]

platform = subprocess.check_output('node --eval "process.stdout.write(process.platform)"', shell=True);
arch = subprocess.check_output('node --eval "process.stdout.write(process.arch)"', shell=True);

print 'precompiling for ' + platform + '/' + arch + '...'

for version in versions:
  # patch node-gyp, while --target does not work: lib/configure.js: versionStr = process.env['NODEGYP_TARGET'] || process.version; 
  os.putenv('NODEGYP_TARGET', version) 
  os.system('node-gyp rebuild')

  out_file = os.path.join('build', 'Release', 'nodetime_native.node')
  if os.path.exists(out_file):
    target_path = os.path.join('..', 'nodetime', 'compiled', platform, arch, version)
    if not os.path.isdir(target_path):
       os.makedirs(target_path)
    shutil.copy(out_file, target_path)

