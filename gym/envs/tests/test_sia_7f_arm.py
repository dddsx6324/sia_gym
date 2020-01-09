import gym
import numpy as np

mode = 'human'
#mode = 'rgb_array'

env = gym.make("SIA7FARMPickAndPlace-v1")

print("action space high: ", env.action_space.high)
print("action space low: ", env.action_space.low)
num_actuator = env.sim.model.nu
print('num_actuator: ', num_actuator)
print('joint names:', env.sim.model.joint_names)
print("gripper pose: ", env.sim.data.get_site_xpos("r_grip_site"), env.sim.data.get_site_xmat("r_grip_site"))
print("qpos: ", env.sim.data.qpos)
env.render('human')

for i in range(20):
  env.reset()
  for i in range(20):
    action = env.action_space.sample()
#     action = np.array([0.0, 0.0, 0.0, -0.5, 0., -1.0]) # 1.0 open -1.0 close

    print("action_space:", env.action_space)
    print("action: ", action)
    obs, reward, done, info = env.step(action)
    print("observation:", obs)
    print("reward:", reward)
    print("done:", done)
    print("info:", info)
    env.render('human')

    print("gripper mocap pos: ", env.sim.data.get_mocap_pos('gripper_r:mocap'))
    print("gripper mocap quat: ", env.sim.data.get_mocap_quat('gripper_r:mocap'))
    print("gripper site xpos and xmat : ", env.sim.data.get_site_xpos("r_grip_site"), env.sim.data.get_site_xmat("r_grip_site"))
    print("number actuator: ", num_actuator)
    print("qpos: ", env.sim.data.qpos)
    print("state: ", env.sim.get_state())
    print("name: ", env.sim.model.name_actuatoradr)
    print("actuator contrl range: ", env.sim.model.actuator_ctrlrange)
    print("body robot0: gripper_link pos and xmat: ", env.sim.data.get_body_xipos("r_gripper_palm_link"), env.sim.data.get_body_xmat("r_gripper_palm_link"))
    # print("site pos: ", env.sim.data.get_site_xpos())
    print("sia joint1: ", env.sim.data.get_joint_qpos("sia_7f_joint1"))
    print("sia joint2: ", env.sim.data.get_joint_qpos("sia_7f_joint2"))
    print("sia joint3: ", env.sim.data.get_joint_qpos("sia_7f_joint3"))
    print("sia joint4: ", env.sim.data.get_joint_qpos("sia_7f_joint4"))
    print("sia joint5: ", env.sim.data.get_joint_qpos("sia_7f_joint5"))
    print("sia joint6: ", env.sim.data.get_joint_qpos("sia_7f_gripper"))
print("env.sim.model.nq: ", env.sim.model.nq)
