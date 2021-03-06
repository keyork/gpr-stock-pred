
import gpytorch

class SpectralMixtureKernelGPModel(gpytorch.models.ExactGP):
    def __init__(self, train_x, train_y, likelihood, num_mixtures):
        super(SpectralMixtureKernelGPModel, self).__init__(train_x, train_y, likelihood)
        self.mean_module = gpytorch.means.ConstantMean()
        self.covar_module = gpytorch.kernels.SpectralMixtureKernel(num_mixtures)
        self.covar_module.initialize_from_data(train_x, train_y)

    def forward(self,x):
        mean_x = self.mean_module(x)
        covar_x = self.covar_module(x)
        return gpytorch.distributions.MultivariateNormal(mean_x, covar_x)
