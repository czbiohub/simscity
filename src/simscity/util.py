
from typing import Union

import numpy as np

import pandas as pd
import scanpy


def arrays_to_anndata(expression: np.ndarray, batch: np.ndarray,
                      classes=np.ndarray, **obsm: np.ndarray):
    """Packages together an AnnData object for use in existing pipelines

    :param expression: array of gene expression
    :param batch: array of batch assignments
    :param classes: array of class (e.g. cell type) assignments
    :param obsm: any other arrays to store as metadata
    :return: AnnData object containing the given data and metadata
    """

    metadata = pd.DataFrame({'batch': batch, 'class': classes})
    metadata['batch'] = metadata['batch'].astype('category')
    metadata['class'] = metadata['class'].astype('category')

    adata = scanpy.AnnData(X=expression, obs=metadata, obsm=obsm)

    return adata