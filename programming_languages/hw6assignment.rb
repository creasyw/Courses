# University of Washington, Programming Languages, Homework 6, hw6runner.rb

# This is the only file you turn in, so do not modify the other files as
# part of your solution.

class MyTetris < Tetris
  # your enhancements here
  def set_board
    @canvas = TetrisCanvas.new
    @board = MyBoard.new(self)
    @canvas.place(@board.block_size * @board.num_rows + 3,
                  @board.block_size * @board.num_columns + 6, 24, 80)
    @board.draw
  end

  def key_bindings
    super
    @root.bind('u', proc{@board.rotate_halfcircle})
    @root.bind('c', proc{@board.cheat})
  end

end

class MyPiece < Piece
  # The constant All_My_Pieces should be declared here
  Cheat_Piece = [[[[0,0]]]]	# for cheating
  All_My_Pieces = All_Pieces + [rotations([[0,0],[1,0],[0,1]]), # tri
  		[[[0, 0], [-1, 0], [1, 0], [2, 0], [3,0]], #longest
  		[[0, 0], [0, -1], [0, 1], [0, 2], [0,3]]],
  		rotations([[0, 0], [1, 0], [0, 1], [1, 1],[2,0]]),
  		rotations([[0, 0], [1, 0], [0, 1], [1, 1],[2,1]])] 

  # your enhancements here
  def self.next_piece (board)
    if !board.cheat_flag
      MyPiece.new(All_My_Pieces.sample, board)
    else
      MyPiece.new(Cheat_Piece.sample, board)
    end
  end

end

class MyBoard < Board
  # your enhancements here
  def initialize (game)
    super
    @current_block = MyPiece.next_piece(self)
    @cheat_flag = false
  end
  def cheat_flag
    @cheat_flag
  end

  def rotate_halfcircle
    if !game_over? and @game.is_running?
      @current_block.move(0, 0, 2)
    end
    draw
  end

  def next_piece
    @current_block = MyPiece.next_piece(self)
    @current_pos = nil
    if @cheat_flag
      @cheat_flag = false
    end
  end
  
  def store_current
    locations = @current_block.current_rotation
    displacement = @current_block.position
    l = locations.length-1
    (0..l).each{|index| 
      current = locations[index];
      @grid[current[1]+displacement[1]][current[0]+displacement[0]] = 
      @current_pos[index]
    }
    remove_filled
    @delay = [@delay - 2, 80].max
  end
  
  def cheat
    if !@cheat_flag and !game_over? and @game.is_running? and @score >=100
      @cheat_flag = true
      @score -= 100
      @game.update_score
    end
  end

end
