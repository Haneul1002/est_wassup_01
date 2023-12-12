import torch
import torch.nn.functional as F
import torchmetrics
from nn import ANN
from sklearn.ensemble import RandomForestRegressor

config = {

   'preprocess' : {
      "features":  ['lane_count', 'road_rating', 'maximum_speed_limit',
                  'weight_restricted', 'month', 'rough_road_name', 
                  'line_number', 'start_latitude_enc', 'end_latitude_enc','end_turn_restricted','start_turn_restricted', 'weight_restricted_enc',
                  "base_hour", "peak_season", 'multi_linked', 'connect_code', 'peak_hour'],
      "train-csv": "/home/data/train_last.csv",
      "test-csv" : "/home/data/test_last.csv",
      "output-train-feas-csv" : "./data/trn_X.csv",
      "output-test-feas-csv" : "./data/tst_X.csv", 
      "output-train-target-csv" : "./data/trn_y.csv", 
      "output-test-target-csv" : "./data/tst_y.csv", 
      "encoding-columns": ['start_turn_restricted', 'end_turn_restricted'],
      "scale-columns" : [], 
      "target-col" : "target",
      "scaler" : "None"
  },
  'wandb':{
      'use_wandb': False,
      'wandb_runname': "12.11: 위도/무게제한 인코딩 컬럼 사용, dropout=True",
      },

  'files': {
    'X_csv': './data/trn_X.csv',
    'y_csv': './data/trn_y.csv',
    'X_test_csv': './data/tst_X.csv',
    'output': './model.pth',
    'output_csv': './results/five_fold.csv',
    'ml_output_model': './ml_model.pkl',
    'submission_csv': './submission.csv',
  },

  'model': ANN, # or RandomForestRegressor
  'ann_model_params': {
    'input_dim': 'auto', # Always will be determined by the data shape
    'hidden_dim': [128, 128, 64, 32],
    'activation': "relu",
    'use_dropout': False,
    'drop_ratio': 0.3,
  },
  
  'ml_model_params':{
      'n_estimators': 40, 
      'min_samples_leaf': 10, 
      'min_samples_split': 10, 
      'random_state': 2022
  },

  'train_params': {
    'data_loader_params': {
      'batch_size': 128,
      'shuffle': True,
    },
    'loss': F.mse_loss,
    'optim': torch.optim.Adam,
    'optim_params': {
      'lr': 0.001,
    },
    'metric': torchmetrics.MeanSquaredError(squared=False),
    'device': 'cuda',
    'epochs': 10,
  },
   
  'cv_params':{
    'n_split': 5,
  },

}
