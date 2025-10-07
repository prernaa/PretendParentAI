import os

DATA_FOLDER = "../../ParentPalAI_Data"

# Original data
POSTS_FPATH = os.path.join(DATA_FOLDER, "Parenting_submissions.json")
COMMENTS_FPATH = os.path.join(DATA_FOLDER, "Parenting_comments.json")

# Datasets generated
CURATED_DATASET_FPATH = os.path.join(DATA_FOLDER, "reddit_dataset.jsonl")
TRAIN_DATASET_FPATH = os.path.join(DATA_FOLDER, "reddit_dataset_train.jsonl")
VAL_DATASET_FPATH = os.path.join(DATA_FOLDER, "reddit_dataset_val.jsonl")
VAL_DATASET_100_FPATH = os.path.join(DATA_FOLDER, "reddit_dataset_val_100.jsonl")

# Datasets uploaded to Github to share with others 
SHARED_DATA_FOLDER = "../data_to_share"
TEST_DATASET_FPATH = os.path.join(SHARED_DATA_FOLDER, "reddit_gpt_test_samples.jsonl")
TEST_DATASET_BASE_FPATH = os.path.join(SHARED_DATA_FOLDER, "reddit_gpt_test_samples_base_response.jsonl")
TEST_DATASET_FT_FPATH = os.path.join(SHARED_DATA_FOLDER, "reddit_gpt_test_samples_ft_response.jsonl")


# Params
MAX_TOKENS = 620

