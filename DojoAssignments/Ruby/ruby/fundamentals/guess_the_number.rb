def guess_number(guess)
  number = 25
  if guess === number
    puts 'You got it'
  end
  if guess < number
    puts 'Guess was too low'
  end
  if guess > number
    puts 'Guess was too high'
  end
end

guess_number(25)
