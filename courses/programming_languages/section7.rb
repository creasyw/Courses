# The 1st program in ruby
class Hello
  def hello_world_method
    puts "Hello, world!"
  end
end

x = Hello.new
x.hello_world_method

# instance variable and class variable
class A
  def initialize(f=0)
    @foo = 0
    @@bar = 0
  end
  def foo=x
    @foo = x
  end
  def m2 (x)
    @foo += x
    @@bar += 1
  end
  def foo
    @foo
  end
  def bar
    @@bar
  end
end

class MyRational
  def initialize(num, den=1)
    if den == 0
      raise "MyRational received an inappropriate argument"
    elsif den<0
      @num = -num
      @den = -den
    else
      @num = num
      @den = den
    end
    reduce
  end

  def to_s
    "#{@num}#{if @den==1 then "" else "/" + @den.to_s end}"
  end

  def add! r
    a = r.num
    b = r.den
    c = @num
    d = @den
    @num = (a*d)+(b*c)
    @den = b*d
    reduce
    self
  end

  def + r
    ans = MyRational.new(@num, @den)
    ans.add! r
    ans
  end

  protected
  def num
    @num
  end
  def den
    @den
  end

  private
  def gcd (x,y)
    if x == y
      x
    elsif x<y
      gcd(x, y-x)
    else
      gcd(y, x)
    end
  end

  def reduce
    if @num == 0
      @den = 1
    else
      d = gcd(@num.abs, @den)
      @num = @num / d
      @den = @den / d
    end
  end
end

def use_rationals
  r1 = MyRational.new(3,4)
  r2 = r1 + r1 + MyRational.new(-5, 2)
  puts r2.to_s
  (r2.add! r1).add! (MyRational.new(1, -4))
  puts r2.to_s
end

