! Use standard ISO C bindings
use, intrinsic :: iso_c_binding
! Use API functions and data structures
use pcmsolver
! Declare handle to API context as C pointer
type(c_ptr) :: pcm_context
! Declare polarization energy as a C-interoperable real number
real(c_double) :: energy
! Initialize API context
pcm_context = pcmsolver_new(...)
! Register surface function from host program to API context
call pcmsolver_set_surface_function(pcm_context, ...)
! Compute the ASC from a MEP surface function
call pcmsolver_compute_asc(pcm_context, ...)
! Retrieve surface function to host from API context
call pcmsolver_get_surface_function(pcm_context, ...)
! Compute polarization energy from surface functions
energy = pcmsolver_compute_polarization_energy(pcm_context, ...)
! Clean up API context
call pcmsolver_delete(pcm_context)
