# SmartRelocator : Saving lives at animal shelters

SmartRelocator enables animal shelters to make data-driven decisions for relocating dogs in order to reduce crowding or in the case of natural disasters 

## Background

Over 6 million animals enter animal shelters in the US every year. However, only half of them are adopted or returned to their owners, leading to crowding in the shelters and unfortunately, euthanization.

![pie_chart](https://github.com/adibhandari/insight/blob/master/extras/pie2.png)


The [ASPCA relocation program](https://www.aspca.org/animal-placement/animal-relocation) provides shelters with the option to relocate their animals to other shelters in nearby states, thus distributing the load. However, this is purely supply and demand based.

SmartRelocator is able to predict adoption times for dogs in various states given their characteristics such as age, size and breed. This allows for optimizing relocation decisions and overall reduce the adoption time for dogs.

## Data

Data for dogs from various states was obtained from the [Petfinder API](https://www.petfinder.com/developers/). Petfinder is the largest online pet adoption website in North America and the API provides access to the Petfinder database of hundreds of thousands of pets in animal shelters in the US.

This was supplemented by state specific information such as population and area from the [US Census Bureau](https://www.census.gov/).

## Directory Structure
```
project
│   README.md
│   LICENSE.md    
│   .gitignore
│
└───extras
│   │   pie2.png
│
└───src
│   │   breedlist_all.csv
│   │   breedlist_all_a4.csv
│   │   stats.csv
│   │   stats_all.csv
│   │
│   └───analysis
│       │   stats_all_combined.ipynb
│       │   stats_all_combined_v2.ipynb
│       │   validation.ipynb
│       │   visualization.ipynb
│       │   ...
│   │
│   └───data_acquisition
│       │   clean_data_all.ipynb
│       │   data_acquisition_by_state.ipynb
│       │   merge_data_all.ipynb
│       │   s3_models.ipynb
│       │   ...
│   │
│   └───model_selection
│       │   final_model.ipynb
│       │   final_model_combined.ipynb
│       │   model_selection_all_A4.ipynb
│       │   model_selection_all_combined_v2.ipynb
│       │   ...
|   
└───webapp
    │   breedlist.csv
    │   relocatortools.py
    │   statelist.csv
    │   Smartrelocator.py
```

## Prerequisites

* Python 3.7
* Jupyter Notebook
* Streamlit
* sklearn
* Plotly
* AWS EC2
* AWS CLI
* boto3


<!-- ## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project. -->

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

This project was done as a part of [Insight](https://www.insightdatascience.com/)

