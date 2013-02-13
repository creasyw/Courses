fun match xs =
  let fun s_need_one xs =
        case xs of
             [] => true
           | 1::xs' => s_need_two xs'
           | _ => false
    and s_need_two xs =
        case xs of
             [] => false
           | 2::xs' => s_need_one xs'
           | _ => false
  in
    s_need_one xs
  end




