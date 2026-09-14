pluginManagement {
	repositories {
		mavenCentral()
		gradlePluginPortal()
		maven {
			name = "GitHubPackages"
			url = uri("https://maven.pkg.github.com/AutoTweaker/core")
			credentials {
				username = providers.gradleProperty("gpr.user").getOrElse("")
				password = providers.gradleProperty("gpr.key").getOrElse("")
			}
		}
	}
}

rootProject.name = "autotweaker-action-test"

include("plugin-a", "plugin-b")
