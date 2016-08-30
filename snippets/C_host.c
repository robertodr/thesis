// Include API functions and data structures definitions
#include "pcmsolver.h"
#include "PCMInput.h"

// Initialize API context
pcmsolver_context_t * pcm_context = pcmsolver_new(...);
// Register surface function from host program to API context
pcmsolver_set_surface_function(pcm_context, ...);
// Compute the ASC from a MEP surface function
pcmsolver_compute_asc(pcm_context, ...);
// Retrieve surface function to host from API context
pcmsolver_get_surface_function(pcm_context, ...);
// Compute polarization energy from surface functions
double energy = pcmsolver_compute_polarization_energy(pcm_context, ...);
// Clean up API context
pcmsolver_delete(pcm_context);
