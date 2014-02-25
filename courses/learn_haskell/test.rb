class Test_Fab
  def generator(n)
    def helper(n0, n1, count)
      if count<=2 then n0 else helper(n0+n1, n0, count-1) end
    end
    helper(1, 1, 3)
  end
end

t = Test_Fab.new
puts t.generator(10)

