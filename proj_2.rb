# Welcome to Sonic Pi

live_loop :blue do
  use_real_time
  a, b, c = sync "/osc*/trigger/blade"
  synth :blade, note: a, cutoff: b, sustain: c
end

live_loop :red do
  use_real_time
  a, b, c = sync "/osc*/trigger/piano"
  synth :piano, note: a, cutoff: b, sustain: c
end

live_loop :blueverb do
  use_real_time
  a, b, c = sync "/osc*/trigger/bladeverb"
  with_fx :reverb, mix: 0.8 do
    synth :blade
    
  end
end

live_loop :redverb do
  use_real_time
  a, b, c = sync "/osc*/trigger/pianoverb"
  with_fx :reverb, mix: 0.6 do
    synth :piano
    
  end
end

live_loop :bluepitch do
  use_real_time
  a, b, c, d = sync "/osc*/trigger/bladepitch"
  with_fx :pitch_shift, pitch: d do
    synth :blade
    
  end
end

live_loop :redpitch do
  use_real_time
  a, b, c, d = sync "/osc*/trigger/pianopitch"
  with_fx :pitch_shift,pitch: d do
    synth :piano
    
  end
end

live_loop :blueall do
  use_real_time
  a, b, c, d = sync "/osc*/trigger/bladeall"
  with_fx :pitch_shift, pitch: d do
    with_fx :reverb, mix: 0.9 do
      synth :prophet
      
    end
  end
end

live_loop :redall do
  use_real_time
  a, b, c, d = sync "/osc*/trigger/pianoall"
  with_fx :pitch_shift,pitch: d do
    with_fx :reverb, mix: 0.6 do
      synth :piano
      
    end
  end
end