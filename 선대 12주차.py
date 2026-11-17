#실습 1 
import numpy as np

u = np.array([[2], [-5], [-1]])
v = np.array([[3], [2], [-3]])

u_dot_v = (u.T @ v).item()
v_dot_u = (v.T @ u).item()

print("u . v =", u_dot_v)
print("v . u =", v_dot_u)
print("교환법칙 확인 :", u_dot_v == v_dot_u)

#실습 2
import numpy as np

u = np.array([1, 2, 4])
v = np.array([2, -3, 5])
w = np.array([4, 2, -3])

print("u . v =", np.dot(u, v))
print("u . w =", np.dot(u, w))
print("v . w =", np.dot(v, w))

#실습3

import numpy as np

u = np.array([1, 2, 3])
v = np.array([-4, 3, 5])

norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

difference = v - u
distance = np.linalg.norm(difference)

print(f"u의 길이 = {norm_u:.6f}")
print(f"v의 길이 = {norm_v:.6f}")
print("v - u =", difference)
print("각 성분의 제곱 =", difference**2)
print(f"두 벡터의 거리 = {distance:.6f}")

#실습4
import numpy as np

u = np.array([2, -5, -1])
v = np.array([-7, -4, 6])

dot_product = np.dot(u, v)

squared_norm_u = np.dot(u, u)

difference = u - v
squared_distance = np.dot(difference, difference)

print("u . v =", dot_product)
print("||u||² =", squared_norm_u)
print("||u-v||² =", squared_distance)

#실습5

import numpy as np

u = np.array([1, 1, 0], dtype=float)
v = np.array([0, 1, 1], dtype=float)

dot_product = np.dot(u, v)
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

distance = np.linalg.norm(u - v)

print(f"내적 = {dot_product:.6f}")
print(f"두 벡터 사이의 거리 = {distance:.6f}")

if norm_u == 0 or norm_v == 0:
    print("영벡터가 포함되어 각도를 정의할 수 없습니다.")
else:
    cos_theta = dot_product / (norm_u * norm_v)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    theta_rad = np.arccos(cos_theta)
    theta_deg = np.degrees(theta_rad)

    print(f"cos(theta) = {cos_theta:.6f}")
    print(f"각도 = {theta_deg:.6f}도")

#실습 6

import numpy as np

u = np.array([1, -1, 0], dtype=float)
v = np.array([2, -1, 2], dtype=float)

dot_product = np.dot(u, v)
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

if norm_u == 0 or norm_v == 0:
    raise ValueError("영벡터가 포함되면 각도를 정의할 수 없습니다.")

cos_theta = dot_product / (norm_u * norm_v)
cos_theta = np.clip(cos_theta, -1.0, 1.0)

theta_rad = np.arccos(cos_theta)
theta_deg = np.degrees(theta_rad)

print(f"내적 = {dot_product:.6f}")
print(f"u의 길이 = {norm_u:.6f}")
print(f"v의 길이 = {norm_v:.6f}")
print(f"cos(theta) = {cos_theta:.6f}")
print(f"각도(라디안) = {theta_rad:.6f}")
print(f"각도(도) = {theta_deg:.6f}도")

#실습7

import numpy as np

u = np.array([1, 2], dtype=float)
v = np.array([6, -3], dtype=float)

dot_product = np.dot(u, v)
norm_u = np.linalg.norm(u)
norm_v = np.linalg.norm(v)

print(f"내적 = {dot_product:.6f}")

if norm_u == 0 or norm_v == 0:
    print("영벡터가 포함되어 각도는 정의되지 않습니다.")
else:
    cos_theta = dot_product / (norm_u * norm_v)
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    theta_deg = np.degrees(np.arccos(cos_theta))
    is_orthogonal = np.isclose(cos_theta, 0.0, atol=1e-10, rtol=0.0)

    print(f"cos(theta) = {cos_theta:.6f}")
    print(f"각도 = {theta_deg:.6f}도")
    print("직교합니다." if is_orthogonal else "직교하지 않습니다.")