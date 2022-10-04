from skimage.exposure import match_histograms
from skimage.exposure import adjust_gamma

def transfer_histogram(base_img, reference_img):
    '''
    Match the histograms of two images.

        Args:
            base_img: image to preserve
            reference_img image to manipulate histogram
        
        Returns:
            result_img: resulting image from match histograms
    '''
    result_img = match_histograms(base_img, reference_img, channel_axis=2)
    return result_img

def adjust_gamma(img):
    '''
    Match the histograms of two images.

        Args:
            img: image to apply correction
        
        Returns:
            result_img: corrected image
    '''
    result_img = adjust_gamma(img)
    return result_img