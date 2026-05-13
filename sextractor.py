import os

from utils import readWriteCats
from terminal import run_command

class SExtr(readWriteCats):
	"""
	Class for running sextractor on an image.

	Args:
	- image (str): Path to the image file.
	- addconf (dict): Dictionary containing additional configurations for sextractor. Default is None.
	- defaultconf (dict): Dictionary containing default configurations for sextractor. Default is None.
	- read_addconf (str): Path to an existing config file to be loaded as additional configurations. Default is None.
	- read_defaultconf (str): Path to an existing config file to be loaded as default configurations. Default is None.
	- folder (str): Folder where the output files will be saved. Default is '/tmp/'.
	- command (str): Path to the sextractor executable file. Default is 'sex'.
	- catname (str): Name of the output catalog file. Default is 'catout.param'.

	Attributes:
	- config (dict): Dictionary containing the sextractor configuration.
	- params (list): List containing the names of the parameters to be extracted by sextractor.
	
	Methods:
	- run(): Runs sextractor with the current configuration and the specified image file.

	"""
	def __init__(self, image=None, outdir='/tmp/', command='sex', catname = "catout.param"):
		readWriteCats.__init__(self)

		self.command = command
		self.image = image
		self.path = outdir

		if outdir:
			if not os.path.exists(outdir):
				os.makedirs(outdir)
				
		
		self.config = {'BACK_FILTERSIZE': {'value': 3, 'comment': ''},
						 'BACK_SIZE': {'value': 64, 'comment': ''},
						 'BACK_TYPE': {'value': 'AUTO', 'comment': ''},
						 'BACK_VALUE': {'value': '0.0,0.0', 'comment': ''},
						 'THRESH_TYPE': {'value': 'RELATIVE', 'comment': ''},
						 'ANALYSIS_THRESH': {'value': 1.5, 'comment': ''},
						 'DETECT_THRESH': {'value': 1.5, 'comment': ''},
						 'DETECT_MINAREA': {'value': 5, 'comment': ''},
						 'FILTER_THRESH': {'value': '', 'comment': ''},
						 'FILTER': {'value': 'Y', 'comment': ''},
						 'FILTER_NAME': {'value': os.path.join('sextr_config/default.conv'), 'comment': ''},
						 'CLEAN': {'value': 'Y', 'comment': ''},
						 'CLEAN_PARAM': {'value': 1.0, 'comment': ''},
						 'DEBLEND_NTHRESH': {'value': 32, 'comment': ''},
						 'DEBLEND_MINCONT': {'value': 0.005, 'comment': ''},
						 'MASK_TYPE': {'value': 'CORRECT', 'comment': ''},
						 'WEIGHT_TYPE': {'value': 'BACKGROUND', 'comment': ''},
						 'WEIGHT_IMAGE': {'value': os.path.join('weight.fits'), 'comment': ''},
						 'WEIGHT_THRESH': {'value': '', 'comment': ''},
						 'WEIGHT_GAIN': {'value': 'Y', 'comment': ''},
						 'GAIN': {'value': 1.0, 'comment': ''},
						 'GAIN_KEY': {'value': 'GAIN', 'comment': ''},
						 'FLAG_IMAGE': {'value': 'flag.fits', 'comment': ''},
						 'FLAG_TYPE': {'value': 'OR', 'comment': ''},
						 'BACKPHOTO_TYPE': {'value': 'LOCAL', 'comment': ''},
						 'BACKPHOTO_THICK': {'value': 24, 'comment': ''},
						 'BACK_FILTTHRESH': {'value': 0.0, 'comment': ''},
						 'PHOT_AUTOPARAMS': {'value': (2.5, 3.5), 'comment': ''},
						 'PHOT_AUTOAPERS': {'value': (0.0, 0.0), 'comment': ''},
						 'PHOT_PETROPARAMS': {'value': (2.0, 3.5), 'comment': ''},
						 'PHOT_APERTURES': {'value': 5, 'comment': ''},
						 'PHOT_FLUXFRAC': {'value': 0.5, 'comment': ''},
						 'SATUR_LEVEL': {'value': 50000.0, 'comment': ''},
						 'SATUR_KEY': {'value': 'SATURATE', 'comment': ''},
						 'STARNNW_NAME': {'value': os.path.join('sextr_config/default.nnw'), 'comment': ''},
						 'SEEING_FWHM': {'value': 3.2, 'comment': ''},
						 'CATALOG_NAME': {'value': os.path.join(outdir, catname), 'comment': ''},
						 'PARAMETERS_NAME': {'value': os.path.join(outdir, 'params.sex'), 'comment': ''},
						 'CHECKIMAGE_TYPE': {'value': 'NONE',
						  'comment': ''},
						 'CHECKIMAGE_NAME': {'value': 'NONE',
						  'comment': ''},
						 'INTERP_TYPE': {'value': 'NONE', 'comment': ''},
						 'INTERP_MAXYLAG': {'value': 4, 'comment': ''},
						 'INTERP_MAXXLAG': {'value': 4, 'comment': ''},
						 'DETECT_TYPE': {'value': 'CCD', 'comment': ''},
						 'MEMORY_BUFSIZE': {'value': 11000, 'comment': ''},
						 'MEMORY_PIXSTACK': {'value': 3000000, 'comment': ''},
						 'MEMORY_OBJSTACK': {'value': 10000, 'comment': ''},
						 'PIXEL_SCALE': {'value': 1.0, 'comment': ''},
						 'MAG_GAMMA': {'value': 4.0, 'comment': ''},
						 'MAG_ZEROPOINT': {'value': 0.0, 'comment': ''},
						 'CATALOG_TYPE': {'value': 'FITS_LDAC', 'comment': ''},
						 'VERBOSE_TYPE': {'value': 'NORMAL', 'comment': ''},
						 'WRITE_XML': {'value': 'Y', 'comment': ''},
						 'XML_NAME': {'value': '/tmp/sexout.xml', 'comment': ''},
						 'NTHREADS': {'value': 1, 'comment': ''}
			}
		
		
		self.params = [
			'NUMBER',
			'X_IMAGE',
			'Y_IMAGE',
			'ELLIPTICITY',
			'ISOAREA_IMAGE',
			'FLAGS',
			'MAG_AUTO',
			'MAGERR_AUTO',
			'FLUX_ISO',
			'FLUXERR_ISO',
			'MAG_ISO',
			'MAGERR_ISO',
			'FLUX_ISOCOR',
			'FLUXERR_ISOCOR',
			'MAG_ISOCOR',
			'MAGERR_ISOCOR',
			'FLUX_RADIUS',
			'FLUX_AUTO',
			'FLUXERR_AUTO',
			'BACKGROUND',
			'FLUX_MAX',
			'FWHM_IMAGE',
			'FWHM_WORLD'
			]
	
 
	def run(self, write_log = True):
		"""Runs sextractor with the current configuration and the specified image file.
		"""        
		if self.image is None:
			return ('Image not found')
		
		self.confile = os.path.join(self.path, 'config.sex')
		self.write_file(self.confile)
		self.write_params()
		
		command = self.command + ' ' + self.image + ' -c ' + self.confile

		out, code = run_command(command)

		if write_log:
			open(os.path.join(self.path, 'sextractor.log'), 'w').write(out)
   
		return out, code