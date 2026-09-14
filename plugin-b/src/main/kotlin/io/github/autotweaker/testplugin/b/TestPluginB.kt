package io.github.autotweaker.testplugin.b

import com.google.auto.service.AutoService
import io.github.autotweaker.api.adapter.Adapter
import io.github.autotweaker.api.adapter.CoreAPI
import io.github.autotweaker.api.types.KebabCase.Companion.toKebab
import io.github.autotweaker.api.types.SemVer
import io.github.autotweaker.api.types.Url.Companion.toUrl
import io.github.autotweaker.api.types.adapter.AdapterInfo

@AutoService(Adapter::class)
class TestPluginB : Adapter {
	private var running = false

	override val isRunning get() = running

	override suspend fun init(core: CoreAPI): AdapterInfo {
		println("[plugin-b] init")
		return AdapterInfo(
			name = "plugin-b".toKebab(),
			description = "Test plugin B",
			version = SemVer.parse("0.1.0"),
			source = "https://github.com/WhiteElephant-abc/autotweaker-action-test".toUrl(),
		)
	}

	override suspend fun start() {
		println("[plugin-b] start")
		running = true
	}

	override suspend fun stop() {
		running = false
	}
}
