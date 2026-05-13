import os 

from utils import readWriteCats
from terminal import run_command

class Scamp(readWriteCats):
	"""
	A class for running Scamp

	Methods
	-------
	run()
		Run Scamp.
	"""
	def __init__(self, catalog, command = "scamp", outdir='/tmp/'):
		"""
		Scamp initialization.

		Parameters
		----------
		catalog : str
			Name of the catalog file.
		outdir : str, optional
			Path to the output directory, by default '/tmp/'.
		addconf : None, optional
			Additional configuration parameters, by default None.
		defaultconf : None, optional
			Default configuration parameters, by default None.
		read_addconf : None, optional
			Read configuration parameters from file, by default None.
		read_defaultconf : None, optional
			Read default configuration parameters from file, by default None.
		"""
		readWriteCats.__init__(self)

		self.command = command
		self.path = outdir
		self.catalog = catalog

		self.config = {
			 'REF_SERVER': {'value': 'vizier.u-strasbg.fr',
			  'comment': ' viziersaao.chpc.ac.za'},
			 'REF_TIMEOUT': {'value': '10',
			  'comment': 'Server connection timeouts (s) 0=none'},
			 'ASTREF_CATALOG': {'value': 'GAIA-DR3', 'comment': ' PANSTARRS-1, or ALLWISE'},
			 'ASTREF_BAND': {'value': 'DEFAULT',
			  'comment': ' or DEFAULT, BLUEST, or REDDEST'},
			 'ASTREFCAT_NAME': {'value': 'astrefcat.cat',
			  'comment': 'Local astrometric reference catalogs'},
			 'ASTREFCENT_KEYS': {'value': 'X_WORLD,Y_WORLD',
			  'comment': 'Local ref.cat. centroid parameters'},
			 'ASTREFERR_KEYS': {'value': 'ERRA_WORLD, ERRB_WORLD, ERRTHETA_WORLD',
			  'comment': ' Local ref.cat. err. ellipse params'},
			 'ASTREFPROP_KEYS': {'value': 'PMALPHA_J2000, PMDELTA_J2000',
			  'comment': 'Local ref.cat. PM params'},
			 'ASTREFPROPERR_KEYS': {'value': 'PMALPHAERR_J2000, PMDELTAERR_J2000',
			  'comment': ' Local ref.cat. PM err. params'},
			 'ASTREFMAG_KEY': {'value': 'MAG',
			  'comment': 'Local ref.cat. magnitude parameter'},
			 'ASTREFMAGERR_KEY': {'value': 'MAGERR',
			  'comment': 'Local ref.cat. mag. error parameter'},
			 'ASTREFOBSDATE_KEY': {'value': 'OBSDATE',
			  'comment': 'Local ref.cat. obs. date parameter'},
			 'ASTREFMAG_LIMITS': {'value': '-99.0,14.0',
			  'comment': 'Select magnitude range in ASTREF_BAND'},
			  
			 'SAVE_REFCATALOG': {'value': 'N',
			  'comment': 'Save ref catalogs in FITS-LDAC format?'},
			 'REFOUT_CATPATH': {'value': self.path,
			  'comment': 'Save path for reference catalogs'},
			 'MERGEDOUTCAT_TYPE': {'value': 'NONE',
			  'comment': 'NONE, ASCII_HEAD, ASCII, FITS_LDAC'},
			 'MERGEDOUTCAT_NAME': {'value': 'merged.cat',
			  'comment': 'Merged output catalog filename'},
			 'SAVE_DGEOMAP': {'value': 'N',
			  'comment': 'Save differential geometry maps (Y/N)?'},
			 'DGEOMAP_NAME': {'value': 'dgeo.fits',
			  'comment': 'Differential geometry map filename'},
			 'DGEOMAP_STEP': {'value': '2', 'comment': 'Map sampling step'},
			 'DGEOMAP_NNEAREST': {'value': '21', 'comment': 'Number of nearest neighbors'},
			 'FULLOUTCAT_TYPE': {'value': 'NONE',
			  'comment': 'NONE, ASCII_HEAD, ASCII, FITS_LDAC'},
			 'FULLOUTCAT_NAME': {'value': 'full.cat',
			  'comment': 'Full output catalog filename'},
			 'MATCH': {'value': 'Y', 'comment': 'Do pattern-matching (Y/N) ?'},
			 'MATCH_NMAX': {'value': '0', 'comment': ' (0=auto)'},
			 'PIXSCALE_MAXERR': {'value': '1.2',
			  'comment': 'Max scale-factor uncertainty'},
			 'POSANGLE_MAXERR': {'value': '5.0',
			  'comment': 'Max position-angle uncertainty (deg)'},
			 'POSITION_MAXERR': {'value': '1.0',
			  'comment': 'Max positional uncertainty (arcmin)'},
			 'MATCH_RESOL': {'value': '0',
			  'comment': 'Matching resolution (arcsec); 0=auto'},
			 'MATCH_FLIPPED': {'value': 'N',
			  'comment': 'Allow matching with flipped axes?'},
			 'MOSAIC_TYPE': {'value': 'UNCHANGED', 'comment': ' FIX_FOCALPLANE or LOOSE'},
			 'FIXFOCALPLANE_NMIN': {'value': '1',
			  'comment': 'Min number of dets for FIX_FOCALPLANE'},
			 'CROSSID_RADIUS': {'value': '2.0',
			  'comment': 'Cross-id initial radius (arcsec)'},
			 'SOLVE_ASTROM': {'value': 'Y',
			  'comment': 'Compute astrometric solution (Y/N) ?'},
			 'PROJECTION_TYPE': {'value': 'SAME', 'comment': 'SAME, TPV or TAN'},
			 'ASTRINSTRU_KEY': {'value': 'FILTER',
			  'comment': 'FITS keyword(s) defining the astrom'},
			 'STABILITY_TYPE': {'value': 'INSTRUMENT',
			  'comment': 'EXPOSURE, PRE-DISTORTED or INSTRUMENT'},
			 'CENTROID_KEYS': {'value': 'XWIN_IMAGE,YWIN_IMAGE',
			  'comment': 'Cat. parameters for centroiding'},
			 'CENTROIDERR_KEYS': {'value': 'ERRAWIN_IMAGE,ERRBWIN_IMAGE,ERRTHETAWIN_IMAGE',
			  'comment': ' Cat. params for centroid err ellipse'},
			 'DISTORT_KEYS': {'value': 'XWIN_IMAGE,YWIN_IMAGE',
			  'comment': 'Cat. parameters or FITS keywords'},
			 'DISTORT_GROUPS': {'value': '1,1',
			  'comment': 'Polynom group for each context key'},
			 'DISTORT_DEGREES': {'value': '3', 'comment': 'Polynom degree for each group'},
			 'FOCDISTORT_DEGREE': {'value': '1',
			  'comment': 'Polynom degree for focal plane coords'},
			 'ASTREF_WEIGHT': {'value': '1.0',
			  'comment': 'Relative weight of ref.astrom.cat.'},
			 'ASTRACCURACY_TYPE': {'value': 'SIGMA-PIXEL',
			  'comment': ' or TURBULENCE-ARCSEC'},
			 'ASTRACCURACY_KEY': {'value': 'ASTRACCU',
			  'comment': 'FITS keyword for ASTR_ACCURACY param.'},
			 'ASTR_ACCURACY': {'value': '0.01',
			  'comment': 'Astrom. uncertainty floor parameter'},
			 'ASTRCLIP_NSIGMA': {'value': '3.0',
			  'comment': 'Astrom. clipping threshold in sigmas'},
			 'COMPUTE_PARALLAXES': {'value': 'N',
			  'comment': 'Compute trigonom. parallaxes (Y/N)?'},
			 'COMPUTE_PROPERMOTIONS': {'value': 'N',
			  'comment': 'Compute proper motions (Y/N)?'},
			 'CORRECT_COLOURSHIFTS': {'value': 'N',
			  'comment': 'Correct for colour shifts (Y/N)?'},
			 'INCLUDE_ASTREFCATALOG': {'value': 'Y',
			  'comment': 'Include ref.cat in prop.motions (Y/N)?'},
			 'ASTR_FLAGSMASK': {'value': '0x00fc',
			  'comment': 'Astrometry rejection mask on SEx FLAGS'},
			 'ASTR_IMAFLAGSMASK': {'value': '0x0',
			  'comment': 'Astrometry rejection mask on IMAFLAGS'},
			 'SOLVE_PHOTOM': {'value': 'Y',
			  'comment': 'Compute photometric solution (Y/N) ?'},
			 'MAGZERO_OUT': {'value': '0.0',
			  'comment': 'Magnitude zero-point(s) in output'},
			 'MAGZERO_INTERR': {'value': '0.01',
			  'comment': 'Internal mag.zero-point accuracy'},
			 'MAGZERO_REFERR': {'value': '0.03',
			  'comment': 'Photom.field mag.zero-point accuracy'},
			 'PHOTINSTRU_KEY': {'value': 'FILTER',
			  'comment': 'FITS keyword(s) defining the photom.'},
			 'MAGZERO_KEY': {'value': 'PHOT_C',
			  'comment': 'FITS keyword for the mag zero-point'},
			 'EXPOTIME_KEY': {'value': 'EXPTIME',
			  'comment': 'FITS keyword for the exposure time (s)'},
			 'AIRMASS_KEY': {'value': 'AIRMASS',
			  'comment': 'FITS keyword for the airmass'},
			 'EXTINCT_KEY': {'value': 'PHOT_K',
			  'comment': 'FITS keyword for the extinction coeff'},
			 'PHOTOMFLAG_KEY': {'value': 'PHOTFLAG',
			  'comment': 'FITS keyword for the photometry flag'},
			 'PHOTFLUX_KEY': {'value': 'FLUX_AUTO',
			  'comment': 'Catalog param. for the flux measurement'},
			 'PHOTFLUXERR_KEY': {'value': 'FLUXERR_AUTO',
			  'comment': 'Catalog parameter for the flux error'},
			 'PHOTCLIP_NSIGMA': {'value': '3.0',
			  'comment': 'Photom.clipping threshold in sigmas'},
			 'PHOT_ACCURACY': {'value': '1e-3',
			  'comment': 'Photometric uncertainty floor (frac.)'},
			 'PHOT_FLAGSMASK': {'value': '0x00fc',
			  'comment': 'Photometry rejection mask on SEx FLAGS'},
			 'PHOT_IMAFLAGSMASK': {'value': '0x0',
			  'comment': 'Photometry rejection mask on IMAFLAGS'},
			 'SN_THRESHOLDS': {'value': '10.0,100.0', 'comment': ' high-SN sample'},
			 'FWHM_THRESHOLDS': {'value': '0.0,100.0',
			  'comment': 'FWHM thresholds (in pixels) for sources'},
			 'ELLIPTICITY_MAX': {'value': '0.5', 'comment': 'Max. source ellipticity'},
			 'FLAGS_MASK': {'value': '0x00f0',
			  'comment': 'Global rejection mask on SEx FLAGS'},
			 'WEIGHTFLAGS_MASK': {'value': '0x00ff',
			  'comment': 'Global rejec. mask on SEx FLAGS_WEIGHT'},
			 'IMAFLAGS_MASK': {'value': '0x0',
			  'comment': 'Global rejec. mask on SEx IMAFLAGS_ISO'},
			 'AHEADER_GLOBAL': {'value': os.path.join(self.path, 'scamp.ahead'),
			  'comment': 'Filename of a global input header'},
			 'AHEADER_NAME': {'value': '', 'comment': ' (overrides AHEADER_SUFFIX)'},
			 'AHEADER_SUFFIX': {'value': '.ahead', 'comment': ' input headers'},
			 'HEADER_NAME': {'value': os.path.join(self.path, 'scamp.head'), 'comment': ' (overrides HEADER_SUFFIX)'},
			 'HEADER_SUFFIX': {'value': '.head',
			  'comment': 'Filename extension for output headers'},
			 'HEADER_TYPE': {'value': 'NORMAL', 'comment': 'NORMAL or FOCAL_PLANE'},
			 'CHECKPLOT_CKEY': {'value': 'SCAMPCOL',
			  'comment': 'FITS keyword for PLPLOT field colour'},
			 'CHECKPLOT_DEV': {'value': 'PNG', 'comment': ' JPEG, AQT, PDF or SVG'},
			 'CHECKPLOT_RES': {'value': '0',
			  'comment': 'Check-plot resolution (0 = default)'},
			 'CHECKPLOT_ANTIALIAS': {'value': 'Y',
			  'comment': 'Anti-aliasing using convert (Y/N) ?'},
			 'CHECKPLOT_TYPE': {'value': 'FGROUPS, DISTORTION, ASTR_INTERROR1D',
			  'comment': 'ASTR_INTERROR2D, ASTR_INTERROR1D, ASTR_REFERROR2D, ASTR_REFERROR1D, ASTR_CHI2, PHOT_ERROR'},
			 'CHECKPLOT_NAME': {'value': os.path.join(self.path, 'fgroups') + "," + os.path.join(self.path, 'distort') + "," + os.path.join(self.path, 'astr_interror1d'),
			  'comment': 'Check-plot filename(s), astr_interror2d, astr_interror1d, astr_referror2d, astr_referror1d, astr_chi2, psphot_error'},
			 'CHECKIMAGE_TYPE': {'value': 'NONE',
			  'comment': 'NONE, AS_PAIR, AS_REFPAIR, or AS_XCORR'},
			 'CHECKIMAGE_NAME': {'value': 'check.fits',
			  'comment': 'Check-image filename(s)'},
			 'VERBOSE_TYPE': {'value': 'NORMAL', 'comment': 'QUIET, NORMAL, LOG or FULL'},
			 'WRITE_XML': {'value': 'N', 'comment': 'Write XML file (Y/N)?'},
			 'XML_NAME': {'value': os.path.join(self.path, 'scamp.xml'), 'comment': 'Filename for XML output'},
			 'XSL_URL': {'value': 'file:///usr/share/scamp/scamp.xsl',
			  'comment': ' Filename for XSL style-sheet'},
			 'NTHREADS': {'value': 0, 'comment': ' 0 = automatic'}}


	def run(self, write_log = True):
		"""
		Run Scamp.
		"""

		if self.catalog is None:
			return ('Catalog not found')
		
		self.confile = os.path.join(self.path, 'config.scamp')
		self.write_file(self.confile, mode='scamp')

		command = self.command + ' ' + self.catalog + ' -c ' + self.confile
		out, code = run_command(command)
  
		if write_log:
			open(os.path.join(self.path, 'scamp.log'), 'w').write(out)
		return out, code


def read_scamp_out(path):
	"""
    Reads the header information from a SCAMP output file and returns a list of
    lists, where each sublist contains the name, value, and comment for a single
    header entry.

    Args:
        path (str): The path to the SCAMP output file to read.

    Returns:
        list: A list of lists, where each sublist contains the name, value, and
        comment for a single header entry.

    Raises:
        FileNotFoundError: If the specified file path does not exist.

    Example:
        >>> readScampHead('/path/to/my/file.fits.head')
        [['SIMPLE', 'T', 'file conforms to FITS standard'],
         ['BITPIX', '-32', 'number of bits per data pixel'],
         ['NAXIS', '2', 'number of data axes'],
         ['NAXIS1', '1300', 'length of data axis 1'],
         ['NAXIS2', '1000', 'length of data axis 2'],
         ['EXTEND', 'T', 'FITS dataset may contain extensions'],
         ...
        ]
    """

	file = open(path, 'r')
	lines = file.readlines()

	contents = []

	for line in lines:
		fsplit = (line.split("="))
		name = fsplit[0]
		
		
		if "HISTORY" in name or "COMMENT" in name or "END" in name:
			pass
		else:
			name = name.strip()
			content = fsplit[1]
			content = content.split("/")
			
			value = content[0].strip().strip("'")
			comment = content[1].strip().strip("\n")
			
			contents.append([name, value, comment])

	return contents