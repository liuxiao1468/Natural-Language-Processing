# CSE576-nlp-visual_relation 
## Contributor: Ziming Dong ##
## Dataset: Visual Genome https://visualgenome.org/ ##
### Task Assigned
* Visual Genome (Simply convert into the required format) + Image Augmentations (Flip, Rotate etc.) +  Language Augmentations (Back-translation, negations etc.) OR Visual Navigation (Simply convert into the required format) + Image Augmentations (Flip, Rotate etc.) +  Language Augmentations (Back-translation, negations etc.) 
### Contribution
* There are three ipynb files, the **example_image_augmentation.ipynb** and **example_word_augmentation.ipynb** shows that I used different APIs to do the image augmentation and annotation augmentation work. After I clear the best API to do the data augmentation work, I used them to create the new dataset in **final_data_creation.ipynb**. Those APIs are: **visual_genome**, **imgaug**, **nlpaug**.
* For the new image creation, I create about 2700 images with using imgaug API, visual_genome API provided all iamges and annotation function, so I extract images and text information without downloading them. For the first 500 images, I flip the original image horizontally. For the 500th-1000th image, I flip the original image horizontally and add additiveGaussianNoise to get new images. For the 1000th-1500th images I use AddtoHue augmentor to augment the original image. For the 1500th-2000th images, I use both flip and AddtoHue augmentors to create new images. For the 2000th-2700th images, I use flip, AddtoHue and additiveGaussianNoise augmentor to create those new images.
*  For the relationship augmentation work, I use nlpaug API and the **relationship_aliases.txt** to create new expression of relationship between objects. Becasue I partition the datasets for several parts, I randomly use nlpaug augmenter to recreate the relationship, such as nlpaug.augmenter.char, nlpaug.augmenter.word, and nlpaug.augmenter.sentence or the relationship_aliases.txt file to replace the old relationship to the new one based on the synonyms words.
### Instruction of API environment/packages
* To run the code files, attched github links give instruction of downloading the dependeces/packages for **visual_genome**, **imgaug**, **nlpaug**. 
* visual_genome: https://github.com/ranjaykrishna/visual_genome_python_driver
* imgaug: https://github.com/aleju/imgaug
* nlpaug: https://github.com/makcedward/nlpaug
