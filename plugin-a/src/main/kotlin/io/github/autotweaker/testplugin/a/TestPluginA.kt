package io.github.autotweaker.testplugin.a

import com.google.auto.service.AutoService
import io.github.autotweaker.api.adapter.Adapter
import io.github.autotweaker.api.adapter.CoreAPI
import io.github.autotweaker.api.types.KebabCase.Companion.toKebab
import io.github.autotweaker.api.types.SemVer
import io.github.autotweaker.api.types.Url.Companion.toUrl
import io.github.autotweaker.api.types.adapter.AdapterInfo

@AutoService(Adapter::class)
class TestPluginA : Adapter {
	private var running = false

	override val isRunning get() = running

	override suspend fun init(core: CoreAPI): AdapterInfo {
		println("[plugin-a] init")
		return AdapterInfo(
			name = "plugin-a".toKebab(),
			description = "Test plugin A",
			version = SemVer.parse("0.1.0"),
			source = "https://github.com/WhiteElephant-abc/autotweaker-action-test".toUrl(),
		)
	}

	override suspend fun start() {
		println("[plugin-a] start")
		running = true
	}

	override suspend fun stop() {
		running = false
	}
}
