plugins {
	kotlin("jvm") version "2.4.10"
	kotlin("kapt") version "2.4.10"
	kotlin("plugin.serialization") version "2.4.10"
	id("io.github.autotweaker.plugin.sdk") version "0.2.0-alpha.7+5d41fd9a"
}

kotlin {
	jvmToolchain(25)
}

repositories {
	mavenCentral()
	maven {
		name = "GitHubPackages"
		url = uri("https://maven.pkg.github.com/AutoTweaker/core")
		credentials {
			username = providers.gradleProperty("gpr.user").getOrElse("")
			password = providers.gradleProperty("gpr.key").getOrElse("")
		}
	}
}

dependencies {
	implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.11.0")
	implementation("org.jetbrains.kotlinx:kotlinx-coroutines-core:1.11.0")
	implementation("com.google.auto.service:auto-service-annotations:1.1.1")
	kapt("com.google.auto.service:auto-service:1.1.1")
}
