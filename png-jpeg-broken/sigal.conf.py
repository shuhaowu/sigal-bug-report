title = "Test Gallery"
source = "gallery"
theme = "photoswipe"

# Use originals in gallery (default: False). If True, this will bypass all
# processing steps (resize, auto-orient, recompress, and any plugin-specific
# step).
# Originals will be symlinked if orig_link = True, else they will be copied.
# use_orig = True

img_format = "JPEG"
img_size = (3000, 2000)
keep_orig = True

jpg_options = {
  'quality': 90,
  'optimize': True,
  'progressive': True,
}

plugins = [
  "sigal.plugins.zip_gallery",
  # "PIL.PngImagePlugin",
  # "PIL.JpegImagePlugin",
]

# zip_gallery = True
# zip_media_format = "orig"
