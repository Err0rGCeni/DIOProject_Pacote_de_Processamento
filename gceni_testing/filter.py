from skimage.filters import sobel
from skimage.filters import laplace

def apply_sobel(img):
    '''
    Apply sobel filter.

        Args:
            img: image to apply sobel
        
        Returns:
            result_img: resulting image from sobel filter
    '''
    result_img = sobel(img)
    return result_img

def apply_laplace(img):
    '''
    Apply laplace filter.

        Args:
            img: image to apply laplace
        
        Returns:
            result_img: resulting image from laplace filter
    '''
    result_img = laplace(img)
    return result_img