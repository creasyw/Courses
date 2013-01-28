
fun is_older (date1:int*int*int, date2:int*int*int) =
  (#1 date1 < #1 date2) orelse (#2 date1 < #2 date2) orelse (#3 date1 < #3
  date2)

fun number_in_month (dates: (int*int*int) list, month:int) =
  if null dates
  then 0
  else 
    if #2 (hd dates) = month
    then 1+number_in_month(tl dates, month)
    else number_in_month(tl dates, month)

fun number_in_months (dates:(int*int*int) list, months:int list) =
  if null months
  then 0
  else number_in_month(dates, hd months)+number_in_months(dates,tl months)

fun dates_in_month (dates:(int*int*int) list, month:int) =
  if null dates
  then []
  else
    if #2 (hd dates) = month
    then (hd dates) :: dates_in_month(tl dates, month)
    else dates_in_month(tl dates, month)

fun dates_in_months (dates:(int*int*int) list, months:int list) =
  if null months
  then []
  else dates_in_month(dates, hd months) @ dates_in_months(dates, tl months)

fun get_nth (x: string list, y: int) =
  if y = 1
  then hd x
  else get_nth(tl x, y-1)

fun date_to_string (date:int*int*int) =
  let
    val months = ["January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"]
  in
    get_nth(months, #2 date)^" "^Int.toString(#3 date)^", "^Int.toString(#1
    date)
  end

fun number_before_reaching_sum (sum:int, nums:int list) =
  if sum-(hd nums) > 0
  then 1+number_before_reaching_sum(sum-(hd nums), (tl nums))
  else 0

fun what_month (day:int) =
  let
    val days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  in
    1+number_before_reaching_sum(day, days)
  end


fun month_range (day1:int, day2:int) =
  if day1 > day2
  then []
  else
    what_month(day1)::month_range(day1+1,day2)

fun oldest (dates:(int*int*int) list) =
  if null dates
  then NONE
  else if null (tl dates)
  then SOME(hd dates)
  else
    let val temp = oldest(tl dates)
    in
      if is_older(hd dates, valOf temp)
      then SOME(hd dates)
      else temp
    end

fun identical_list (x:int list) =
  if null x
  then []
  else
    let
      fun is_identical (v:int, y:int list) =
        (null y) orelse ((v<>(hd y)) andalso is_identical(v, tl y))
    in
      if is_identical(hd x, tl x)
      then (hd x)::identical_list(tl x)
      else identical_list(tl x)
    end

fun number_in_months_challenge (dates:(int*int*int) list, months:int list) =
  number_in_months(dates, identical_list(months))

fun dates_in_months_challenge (dates:(int*int*int) list, months:int list) =
  dates_in_months(dates, identical_list(months))


fun reasonable_date (date: (int * int * int)) =
    let
        fun get_days (ns: int list, n: int) =
            if n = 1 then hd ns
            else get_days (tl ns, n - 1)

        val days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        val (y, m, d) = date
    in
        if (y < 1) orelse (m < 1) orelse (m > 12) orelse (d < 1) then false
        else let
                 val leap_year = (y mod 4 = 0) andalso (y mod 100 > 0) orelse (y mod 400 = 0)
                 val add_day = if leap_year andalso (m = 2) then 1 else 0
             in
                 d <= get_days (days, m) + add_day
             end
    end

