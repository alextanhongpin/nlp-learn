
## Clustering document similarity

- in order to find the similarity of the documents, we need to compute the similarity score between each documents
- this is a n^2 operation - for each document, we need to calculate the similarity against all other documents (only new existing ones)
- how can we reduce the comparison?
- say we have a document with the given category, we can just compare to other documents with the same category
- if the document does not share even one similar text, we can conclude they are not similar at all (?)


## Algorithms

- SpotSigs
- LSH (locality-sensitive-hashing)
- Shingles.
- I-Match
- SimHash (used by Google)


## References

- https://en.wikipedia.org/wiki/SimHash
- https://leons.im/posts/a-python-implementation-of-simhash-algorithm/
- https://arxiv.org/pdf/1810.03102.pdf
- https://medium.com/@adriensieg/text-similarities-da019229c894
- https://medium.com/wbaa/https-medium-com-ingwbaa-boosting-selection-of-the-most-similar-entities-in-large-scale-datasets-450b3242e618
- https://www.researchgate.net/publication/234079745_Near_Duplicate_Document_Detection_for_Large_Information_Flows
