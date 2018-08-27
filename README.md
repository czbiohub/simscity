# Welcome to Sim S(single)-C(ellular)ity

The intention of this repo is to factor out code used to simulate scRNA data. Rather than writing it many times for many uses, we can write it one time and incorporate many features into our simulator. 

Examples of data that we might want to generate:

 - A particular type of latent space to test if we can learn it
 - A given batch structure to test if we can correct for it
 - Counts sampled according a given model, to test if the underlying sample can be recovered
 - Data associated with a phenotype to see if our models can learn that relationship (using the same generative model or otherwise)
