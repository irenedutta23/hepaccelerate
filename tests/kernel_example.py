import uproot, os
use_cuda = int(os.environ.get("HEPACCELERATE_CUDA", 0))==1

if use_cuda:
  import hepaccelerate.backend_cuda as ha
  import cupy as anp
  import numpy as np
else:
  import hepaccelerate.backend_cpu as ha
  import numpy as anp
  import numpy as np
  anp.asnumpy = anp.array

fi = uproot.open("data/nanoaod_test.root")
tt = fi.get("Events")
jet_eta = tt.array("Jet_eta")
jet_phi = tt.array("Jet_phi")
jet_pt = tt.array("Jet_pt")

lep_eta = tt.array("Muon_eta")
lep_phi = tt.array("Muon_phi")
lep_pt = tt.array("Muon_pt")

jets = {"pt": anp.array(jet_pt.content), "eta": anp.array(jet_eta.content), "phi": anp.array(jet_phi.content), "offsets": anp.array(jet_pt.offsets)}
sel_jets = jet_pt.content > 30.0

leptons = {"pt": anp.array(lep_pt.content), "eta": anp.array(lep_eta.content), "phi": anp.array(lep_phi.content), "offsets": anp.array(lep_pt.offsets)}
sel_leptons = lep_pt.content > 20.0

#run multithreaded CPU kernels
max_jet_pt = ha.max_in_offsets(jets["offsets"], jets["pt"])

#compare with awkward-array
m1 = anp.asnumpy(max_jet_pt)
m2 = jet_pt.max()
m2[np.isinf(m2)] = 0
assert(np.all(m1 == m2))
 
masked_jets = ha.mask_deltar_first(jets, sel_jets, leptons, sel_leptons, 0.5)
print("kept {0} jets out of {1}".format(masked_jets.sum(), len(masked_jets)))
