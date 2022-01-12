// fused1.stan
data {
   int<lower=1> T;
   matrix[T,T] X;
   vector[T] Y;
   real<lower=0> Lambda;
}
parameters {
   vector[T] beta;
}
transformed parameters {
  vector[T-1] beta_d1;
  real<lower=0> squared_error;
  beta_d1 = beta[1:T-1] - beta[2:T];
  squared_error = dot_self(Y - X * beta);
}
model {
  target += -squared_error;
  for (k in 1:(T-1))
    target += -Lambda * fabs(beta_d1[k]);
}