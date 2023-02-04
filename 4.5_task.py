import re

telescope_text = "The Hubble.Space.Telescope (often referred to as HST or Hubble) is a space telescope that was launched into low Earth orbit in 1990 and remains in operation.... It was not the first space telescope, but it is one of the largest and most versatile, renowned both as a vital research tool and as a public relations boon for astronomy. The Hubble telescope is named after astronomer Edwin Hubble and is one of NASA's Great Observatories..... The Space Telescope Science Institute (STScI) selects Hubble's targets and processes the resulting data, while the Goddard Space Flight Center (GSFC) controls the spacecraft.A commission headed by Lew Allen, director of the Jet Propulsion Laboratory, was established to determine how the error could have arisen. The Allen Commission found that a reflective null corrector, a testing device used to achieve a properly shaped non-spherical mirror, had been incorrectly assembled—one lens was out of position by 1.3 mm (0.051 in)."

edited1_text = re.sub(r'(\.{4,}\s)', '.\n', telescope_text)
edited2_text = re.sub(r'(?<!\. [A-Z])(?=\. [A-Z])', '.\n', edited1_text)
edited3_text = re.sub(r'(\s\.\s)', '\n', edited2_text)
final_text = re.sub(r'\.A', '.\nA', edited3_text)
#print(edited3_text)
telescope_list = final_text.split('\n')
print(telescope_list)
