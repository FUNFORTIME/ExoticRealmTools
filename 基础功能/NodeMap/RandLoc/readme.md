# 均匀点生成技术详解

## 1. 平行四边形区域

### 数学原理

平行四边形内和边界的点可以通过两个基向量的线性组合来表示：

$$
P(u,v) = A + u \cdot \vec{AB} + v \cdot \vec{AD}, \quad u,v \in [0,1]
$$

其中：

- $A$ 是起点坐标
- $\vec{AB}$ 和 $\vec{AD}$ 是两个边向量
- $u,v $ ~$U(0,1)$

### 均匀性证明

从参数空间 $(u,v)$ 到物理空间 $(x,y)$ 的雅可比行列式为常数：

$$
|J| = \left| \frac{\partial(x,y)}{\partial(u,v)} \right| = |\vec{AB} \times \vec{AD}| = S
$$

因此直接在 $[0,1]^2$ 上均匀采样 $(u,v)$ 即可保证在平行四边形内均匀分布。

---

## 2. 三角形区域

### 数学原理

使用重心坐标系统（平面向量基本定理即可证明）：

$$
P = \alpha A + \beta B + \gamma C
$$

约束条件：

$$
\alpha + \beta + \gamma = 1, \quad \alpha, \beta, \gamma \geq 0
$$

参数化表示：

$$
\alpha = 1 - u, \quad \beta = u(1 - v), \quad \gamma = uv
$$

### 关键变换

平方根变换：

$$
\alpha= 1 - s_1;  \beta =(1 - r_2)  s_1 ;  \gamma = r_2  s_1;
$$

其中：

- $r_1,r_2 $ ~$U(0,1)$
- $s_1 = \sqrt{r_1}$

### 均匀性证明

参数域为 $u \geq 0, v \geq 0, u + v \leq 1$，边际分布为：

$$
f_U(u) = 2(1 - u)
$$

通过累积分布函数变换：

$$
F_U(u) = \int_0^u 2(1 - s) ds = 2u - u^2
$$

令 $F_U(u) = r_1$，解得：

$$
u = 1 - \sqrt{1 - r_1} = 1 - \sqrt{r_1'}
$$

### 上面的证明与坐标维数无关（三个不共线的点确定唯一平面）

---

## 3. 圆形区域

### 数学原理

极坐标表示：

$$
x = r \cos\theta, \quad y = r \sin\theta
$$

面元：

$$
dA = r dr d\theta
$$

### 关键变换

半径平方根变换：

$$
r= R\sqrt{\rho};  
$$

其中：

- $\rho$ ~$U(0,1)$
- $\theta$ ~$U(0,2\pi)$

### 均匀性证明

概率密度变换

$$
f(r,\theta) = f(x,y) \cdot |J| = \frac{1}{\pi R^2} \cdot r
$$

通过累积分布函数：

$$
F(r) = \frac{\pi r^2}{\pi R^2} = \left(\frac{r}{R}\right)^2 = \rho
$$

解得：

$$
r = R \sqrt{\rho}
$$

### 椭圆仿射变换即可。球形需开三次方根

作者：仓库维护者

测试
