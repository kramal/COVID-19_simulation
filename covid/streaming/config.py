import numpy as np

initial_params = 5
nodes_num = 17
sim_len = 100
run_iteration = False
region = 0
is_finished = False
nodes_old = []
new_plot_all = []
iteration_over = False
new_nodes_all = []
state_sus = []
state_exp = []
state_inf = []
state_sin = []
state_qua = []
state_imm = []
state_dea = []
newx = []
counter = 1
counter_func = 0

#  from Mukhamet Parameters
param_beta_exp = 0.2*np.ones(nodes_num)     # Susceptible to exposed transition constant
param_qr  = 0.02*np.ones(nodes_num)         # Daily quarantine rate (Ratio of Exposed getting Quarantined)
param_sir  = 0.01*np.ones(nodes_num)        # Daily isolation rate (Ratio of Infected getting Isolated)

param_eps_exp = 0.7*np.ones(nodes_num)       # Disease transmission rate of exposed compared to the infected
param_eps_qua = 0.3*np.ones(nodes_num)       # Disease transmission rate of quarantined compared to the infected
param_eps_sev  = 0.3*np.ones(nodes_num)       # D  isease transmission rate of isolated compared to the infected

param_hosp_capacity = 3000*np.ones(nodes_num)   # Maximum amount patients that hospital can accommodate

param_gamma_mor1 = 0.03*np.ones(nodes_num) # Severe Infected (Hospitalized) to Dead transition probability
param_gamma_mor2 = 0.1*np.ones(nodes_num) # Severe Infected (Not Hospitalized) to Dead transition probability
param_gamma_im = 0.9*np.ones(nodes_num)      # Infected to Recovery Immunized transition probability

param_sim_len = 2*np.ones(nodes_num)            # Length of simulation in days

param_t_exp = 5*np.ones(nodes_num)             # Incubation period (The period from the start of incubation to the end of the incubation state
param_t_inf = 8*np.ones(nodes_num)             # Infection period (The period from the start of infection to the end of the infection state

param_init_exposed = 10*np.ones(nodes_num) # np.array([100,100,100])#10*np.ones(nodes_num)

param_transition_leakage = 0.0
param_transition_scale = 1.0

# Init values for nodes constant
param_init_susceptible = np.squeeze(np.array([1854556,2039379,738587,869603,633801,652314,1125297,678224,1078362,753804,1378554,872736,794165,1378504,1011511,554519,1981747]))

params_network = []
params_node = []

params_old = []

testing_var = []

box1 = list(range(0, 17))
box2 = list(range(0, 17))
box3 = list(range(0, 17))

loop_num = 2

param_transition_box = []
param_transition_box.append(box1)
param_transition_box.append(box2)
param_transition_box.append(box3)

transition_matrix = 0.5*np.array([[0.000000000000000000e+00,5.100000000000000000e+03,0.000000000000000000e+00,8.240000000000000000e+02,6.530000000000000000e+02,6.680000000000000000e+02,1.281000000000000000e+03,6.880000000000000000e+02,1.193000000000000000e+03,7.440000000000000000e+02,1.352000000000000000e+03,8.260000000000000000e+02,8.930000000000000000e+02,1.532000000000000000e+03,1.454000000000000000e+03,0.000000000000000000e+00,2.400000000000000000e+02],
[5.100000000000000000e+03,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,9.870000000000000000e+02,0.000000000000000000e+00,1.200000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,6.000000000000000000e+01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00],
[0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,4.610000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,4.780000000000000000e+02,2.057000000000000000e+03,0.000000000000000000e+00,1.800000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00],
[8.240000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,4.950000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,5.150000000000000000e+02,6.510000000000000000e+02,0.000000000000000000e+00,7.200000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00],
[6.530000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,4.950000000000000000e+02,0.000000000000000000e+00,6.150000000000000000e+02,0.000000000000000000e+00,4.430000000000000000e+02,5.400000000000000000e+02,0.000000000000000000e+00,5.870000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,5.260000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00],
[6.680000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,6.150000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,4.490000000000000000e+02,5.490000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00],
[1.280000000000000000e+03,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,7.440000000000000000e+02,0.000000000000000000e+00,6.000000000000000000e+01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00],
[6.880000000000000000e+02,0.000000000000000000e+00,4.780000000000000000e+02,5.150000000000000000e+02,5.030000000000000000e+02,4.490000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,5.630000000000000000e+02,0.000000000000000000e+00,1.034000000000000000e+03,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,5.490000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00],
[1.193000000000000000e+03,1.042000000000000000e+03,2.057000000000000000e+03,6.510000000000000000e+02,5.400000000000000000e+02,5.490000000000000000e+02,7.440000000000000000e+02,5.630000000000000000e+02,0.000000000000000000e+00,6.600000000000000000e+02,1.768000000000000000e+03,6.520000000000000000e+02,7.980000000000000000e+02,1.057000000000000000e+03,7.060000000000000000e+02,7.180000000000000000e+02,0.000000000000000000e+00],
[7.440000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,6.600000000000000000e+02,0.000000000000000000e+00,1.030000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00],
[1.352000000000000000e+03,1.200000000000000000e+02,1.800000000000000000e+02,7.200000000000000000e+02,5.870000000000000000e+02,0.000000000000000000e+00,6.000000000000000000e+01,1.034000000000000000e+03,1.768000000000000000e+03,1.030000000000000000e+02,0.000000000000000000e+00,7.650000000000000000e+02,8.010000000000000000e+02,1.077000000000000000e+03,9.680000000000000000e+02,6.000000000000000000e+01,2.400000000000000000e+02],
[8.260000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,6.520000000000000000e+02,0.000000000000000000e+00,7.650000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00],
[8.920000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,7.980000000000000000e+02,0.000000000000000000e+00,8.010000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00],
[1.532000000000000000e+03,6.000000000000000000e+01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,1.057000000000000000e+03,0.000000000000000000e+00,1.077000000000000000e+03,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00],
[1.454000000000000000e+03,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,5.490000000000000000e+02,7.060000000000000000e+02,0.000000000000000000e+00,9.680000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,4.830000000000000000e+02,9.000000000000000000e+02],
[0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,7.180000000000000000e+02,0.000000000000000000e+00,6.000000000000000000e+01,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,4.830000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00],
[2.400000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,2.400000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00,0.000000000000000000e+00,9.000000000000000000e+02,0.000000000000000000e+00,0.000000000000000000e+00]])

transition_matrix = transition_matrix.astype(int)
