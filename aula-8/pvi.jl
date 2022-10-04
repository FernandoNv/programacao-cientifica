using Plots

function func(t, y)
  dydt = y-t*t+1
  return dydt
end

function main()
  w = zeros(Float64, n+1)
  a = 0.0;
  b = 2.0;
  N:UInt16 = 10;
  y0 = 0.5;
  t,w = euler()
  h = (b-a)/n
  for i=1:n
    w[i+1] = w[i]+h*func(t[i], w[i])
  end
end

main()