using Plots

function func(t, y)
  return y - t*t + 1
end

function ya(t)
  return (t+1)*(t+1)-0.5*ℯ^t
end

function euler(_a, _w0, _h, _N)
  w = zeros(Float64, _N)
  w[1] = _w0
  for i=1: _N-1
    w[i+1] = w[i] + _h * func(_a+i*_h, w[i])
  end
  return w
end

function main()
  println(".main()")
  a = 0.0
  b = 2.0
  h = 0.5
  w0 = 0.5
  N = Int64((b-a)/h)
  we = euler(a, w0, h, N)
  
  t = zeros(Float64, N)
  t[1] = a
  wa = zeros(Float64, N)
  wa[1] = w0;
  for i=1: N-1
    t[i+1] = a + i*h
    wa[i+1] = ya(t[i])
  end

  @show wa
  @show we
end

if length(ARGS) == 0
  println("PROG")
  main()
else
  println("Too many args")
end