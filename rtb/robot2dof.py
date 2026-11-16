import numpy as np
import roboticstoolbox as rtb

# 1. Mo hinh robot bang tham so DH (2 khop quay phang)
L1, L2 = 0.20, 0.15   # chieu dai khau (m)
robot = rtb.DHRobot(
    [rtb.RevoluteDH(a=L1), rtb.RevoluteDH(a=L2)],
    name="Robot2DOF"
)
print(robot)

# 2. Dong hoc thuan: goc khop -> vi tri dau cong tac
q0 = np.deg2rad([30, 45])
T0 = robot.fkine(q0)
print("Vi tri dau cong tac:\n", T0)

# 3. Dong hoc nghich: vi tri mong muon -> goc khop
T_goal = robot.fkine(np.deg2rad([60, -30]))
sol = robot.ikine_LM(T_goal, q0=q0, mask=[1, 1, 0, 0, 0, 0])
print("IK thanh cong:", sol.success, "| goc (do):", np.rad2deg(sol.q))

# 4. Jacobian tai q0
print("Jacobian:\n", robot.jacob0(q0)[:2, :])

# 5. Quy dao tu q0 den nghiem IK va mo phong
traj = rtb.jtraj(q0, sol.q, 50)
robot.plot(traj.q, backend="pyplot", dt=0.05, block=True)
