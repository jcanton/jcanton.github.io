#===============================================================================
# Process images for upload to website
#===============================================================================

#-------------------------------------------------------------------------------
# Import modules
#
import os, subprocess

#-------------------------------------------------------------------------------
# Data
#
searchRoot = 'assets'
imgExtensions = ['ase', 'art', 'bmp', 'blp', 'cd5', 'cit', 'cpt', 'cr2', 'cut', 'dds', 'dib', 'djvu', 'egt', 'exif', 'gif', 'gpl', 'grf', 'icns', 'ico', 'iff', 'jng', 'jpeg', 'jpg', 'jfif', 'jp2', 'jps', 'lbm', 'max', 'miff', 'mng', 'msp', 'nitf', 'ota', 'pbm', 'pc1', 'pc2', 'pc3', 'pcf', 'pcx', 'pdn', 'pgm', 'PI1', 'PI2', 'PI3', 'pict', 'pct', 'pnm', 'pns', 'ppm', 'psb', 'psd', 'pdd', 'psp', 'px', 'pxm', 'pxr', 'qfx', 'raw', 'rle', 'sct', 'sgi', 'rgb', 'int', 'bw', 'tga', 'tiff', 'tif', 'vtf', 'xbm', 'xcf', 'xpm', '3dv', 'amf', 'ai', 'awg', 'cgm', 'cdr', 'cmx', 'dxf', 'e2d', 'egt', 'eps', 'fs', 'gbr', 'odg', 'svg', 'stl', 'vrml', 'x3d', 'sxd', 'v2d', 'vnd', 'wmf', 'emf', 'art', 'xar', 'png', 'webp', 'jxr', 'hdp', 'wdp', 'cur', 'ecw', 'iff', 'lbm', 'liff', 'nrrd', 'pam', 'pcx', 'pgf', 'sgi', 'rgb', 'rgba', 'bw', 'int', 'inta', 'sid', 'ras', 'sun', 'tga']

thumbFileSize = 1   # [B]
thumbHeight   = 500 # [px]
thumbSdir     = 'thumbs'
forceRegen    = False
doNotResize   = []

cmdCleanExif = 'exiftool -overwrite_original -all='
cmdCreateThumb = lambda inF, outF : 'convert {0:s} -filter Triangle -define filter:support=2 -thumbnail x{2:d} -unsharp 0.25x0.25+8+0.065 -dither None -posterize 136 -quality 82 -define jpeg:fancy-upsampling=off -define png:compression-filter=5 -define png:compression-level=9 -define png:compression-strategy=1 -define png:exclude-chunk=all -interlace none -colorspace sRGB -strip {1:s}'.format(inF, outF, thumbHeight)

#-------------------------------------------------------------------------------
# Travel through the directory tree
#
for dirPath, subDirs, fileList in os.walk(searchRoot, followlinks=True):

    if os.path.basename(dirPath) != thumbSdir:

        # List any image files
        imgFiles = [os.path.join(dirPath, f) for f in sorted(fileList)
                if os.path.splitext(f)[1][1:] in imgExtensions]

        print('\nDirectory: ' + dirPath)
        print(imgFiles)

        for imgFile in imgFiles:

            # Clean exif data
            subprocess.run(cmdCleanExif, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            # If file is larger than thumbSize, and is not in the exclusion list,
            # create a duplicate small file
            if ( (os.path.getsize(imgFile) > thumbFileSize)
                    and (os.path.basename(imgFile) not in doNotResize) ):

                thumbDir = os.path.join(os.path.dirname(imgFile), thumbSdir)
                if not os.path.isdir(thumbDir):
                    os.makedirs(thumbDir)

                outImgFile = os.path.join(thumbDir, os.path.basename(imgFile))

                if (not os.path.isfile(outImgFile)) or (forceRegen):
                    subprocess.run(cmdCreateThumb(imgFile, outImgFile), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

                    print('Reducing file size of: ' + os.path.basename(imgFile))
                    print('in {0:7.3f} kB - out {1:7.3f} kB'.format(os.path.getsize(imgFile)/1e3, os.path.getsize(outImgFile)/1e3))
