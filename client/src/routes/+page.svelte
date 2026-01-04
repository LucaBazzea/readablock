<script>
	import { onMount } from 'svelte';

	let selectedWord = '';
	let translation = '';
	let hoveredFeature = null;

	const italianExcerpt = [
		{ text: "C'era", translation: 'There was' },
		{ text: 'una', translation: 'a/an' },
		{ text: 'volta...', translation: 'once...' },
		{ text: '—Un', translation: '—A' },
		{ text: 'pezzo', translation: 'piece' },
		{ text: 'di', translation: 'of' },
		{ text: 'legno.', translation: 'wood.' },
		{ text: 'Non', translation: 'Not' },
		{ text: 'era', translation: 'was' },
		{ text: 'un', translation: 'a' },
		{ text: 'legno', translation: 'wood' },
		{ text: 'di', translation: 'of' },
		{ text: 'lusso,', translation: 'luxury,' },
		{ text: 'ma', translation: 'but' },
		{ text: 'un', translation: 'a' },
		{ text: 'semplice', translation: 'simple' },
		{ text: 'pezzo', translation: 'piece' },
		{ text: 'da', translation: 'from' },
		{ text: 'catasta,', translation: 'woodpile,' },
		{ text: 'di', translation: 'of' },
		{ text: 'quelli', translation: 'those' },
		{ text: 'che', translation: 'that' },
		{ text: "d'inverno", translation: 'in winter' },
		{ text: 'si', translation: 'one' },
		{ text: 'mettono', translation: 'puts' },
		{ text: 'nelle', translation: 'in the' },
		{ text: 'stufe', translation: 'stoves' },
		{ text: 'e', translation: 'and' },
		{ text: 'nei', translation: 'in the' },
		{ text: 'caminetti', translation: 'fireplaces' },
		{ text: 'per', translation: 'to' },
		{ text: 'accendere', translation: 'light' },
		{ text: 'il', translation: 'the' },
		{ text: 'fuoco', translation: 'fire' },
		{ text: 'e', translation: 'and' },
		{ text: 'per', translation: 'to' },
		{ text: 'riscaldare', translation: 'warm' },
		{ text: 'le', translation: 'the' },
		{ text: 'stanze.', translation: 'rooms.' }
	];

	const features = [
		{
			title: 'Immersive Reading',
			description:
				'Read authentic literature in your target language. Every word is a lesson waiting to be discovered.',
			icon: '📖'
		},
		{
			title: 'Contextual Learning',
			description:
				'Click any word or sentence for instant translation. Learn vocabulary in the context of real stories, not isolated lists.',
			icon: '🎯'
		},
		{
			title: 'Chunking Mastery',
			description:
				"Reinforce learning through our sentence reorganization game. Practice the phrases and patterns you've read.",
			icon: '🧩'
		}
	];

	const pricingPlans = [
		{
			name: 'Free',
			price: '$0',
			period: 'forever',
			features: [
				'3 books available',
				'Basic word translations',
				'50 games per month',
				'Community support'
			],
			cta: 'Start Reading',
			highlighted: false
		},
		{
			name: 'Reader',
			price: '$12',
			period: 'per month',
			features: [
				'Full library access',
				'Unlimited translations',
				'Unlimited games',
				'Sentence analysis',
				'Progress tracking',
				'Priority support'
			],
			cta: 'Begin Your Journey',
			highlighted: true
		},
		{
			name: 'Polyglot',
			price: '$99',
			period: 'per year',
			features: [
				'Everything in Reader',
				'Multiple languages',
				'Custom book uploads',
				'Advanced analytics',
				'Offline mode',
				'Early access features'
			],
			cta: 'Master Languages',
			highlighted: false
		}
	];

	function handleWordClick(word, trans) {
		selectedWord = word;
		translation = trans;
		setTimeout(() => {
			selectedWord = '';
			translation = '';
		}, 2000);
	}

	let scrollY = 0;

	onMount(() => {
		const handleScroll = () => {
			scrollY = window.scrollY;
		};

		window.addEventListener('scroll', handleScroll);

		return () => {
			window.removeEventListener('scroll', handleScroll);
		};
	});
</script>

<svelte:head>
	<title>readablock — Learn Languages Through Immersion</title>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
	<link
		href="https://fonts.googleapis.com/css2?family=Crimson+Text:ital,wght@0,400;0,600;0,700;1,400&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<div class="app-container">
	<!-- Hero Section -->
	<section class="hero-section">
		<div class="hero-content">
			<div class="hero-text">
				<h1 class="hero-title">
					Read.<br />
					Click.<br />
					<span class="gradient-text">Learn.</span>
				</h1>
				<p class="hero-subtitle">
					Master languages through immersive reading. Every word tells a story. Every sentence
					builds fluency.
				</p>
				<div class="hero-cta">
					<a href="/read" class="btn btn-primary">Start Reading</a>
				</div>
			</div>

			<div class="hero-demo">
				<div class="book-preview">
					<div class="book-header">
						<span class="book-title">Le Avventure di Pinocchio</span>
						<span class="book-progress">Chapter 1</span>
					</div>
					<div class="book-content">
						<p class="italian-text">
							{#each italianExcerpt as word, i}
								<button
									class="word"
									class:selected={selectedWord === word.text}
									on:click={() => handleWordClick(word.text, word.translation)}
									style="animation-delay: {i * 0.05}s"
								>
									{word.text}
								</button>
							{/each}
						</p>
						{#if translation}
							<div class="translation-tooltip">
								<span class="tooltip-word">{selectedWord}</span>
								<span class="tooltip-translation">{translation}</span>
							</div>
						{/if}
					</div>
				</div>
			</div>
		</div>

		<div class="scroll-indicator">
			<div class="scroll-line"></div>
			<span>Scroll to explore</span>
		</div>
	</section>

	<!-- Features Section -->
	<section class="features-section">
		<div class="section-header">
			<h2 class="section-title">The Science of Language Immersion</h2>
			<p class="section-subtitle">Three principles. Infinite possibilities.</p>
		</div>

		<div class="features-grid">
			{#each features as feature, i}
				<div
					class="feature-card"
					class:hovered={hoveredFeature === i}
					on:mouseenter={() => (hoveredFeature = i)}
					on:mouseleave={() => (hoveredFeature = null)}
					style="animation-delay: {i * 0.2}s"
				>
					<div class="feature-icon">{feature.icon}</div>
					<h3 class="feature-title">{feature.title}</h3>
					<p class="feature-description">{feature.description}</p>
					<div class="feature-border"></div>
				</div>
			{/each}
		</div>
	</section>

	<!-- How It Works -->
	<section class="how-section">
		<div class="how-content">
			<div class="how-left">
				<h2 class="how-title">From Pages<br />to Fluency</h2>
				<p class="how-description">
					readablock transforms classic literature into your personal language laboratory. Read
					authentic texts, build vocabulary in context, and reinforce learning through play.
				</p>
				<div class="how-stats">
					<div class="stat">
						<div class="stat-number">10,000+</div>
						<div class="stat-label">Words Learned</div>
					</div>
					<div class="stat">
						<div class="stat-number">500+</div>
						<div class="stat-label">Books Available</div>
					</div>
					<div class="stat">
						<div class="stat-number">12</div>
						<div class="stat-label">Languages</div>
					</div>
				</div>
			</div>

			<div class="how-right">
				<div class="process-steps">
					<div class="process-step">
						<div class="step-number">01</div>
						<div class="step-content">
							<h4>Choose Your Book</h4>
							<p>Select from classics like Pinocchio, Don Quixote, or contemporary novels.</p>
						</div>
					</div>
					<div class="process-step">
						<div class="step-number">02</div>
						<div class="step-content">
							<h4>Read & Discover</h4>
							<p>Click any word or sentence for instant translation and context.</p>
						</div>
					</div>
					<div class="process-step">
						<div class="step-number">03</div>
						<div class="step-content">
							<h4>Practice Chunking</h4>
							<p>Reorganize sentences from your reading to master sentence patterns.</p>
						</div>
					</div>
					<div class="process-step">
						<div class="step-number">04</div>
						<div class="step-content">
							<h4>Track Progress</h4>
							<p>Watch your vocabulary grow and fluency improve over time.</p>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- Pricing Section -->
	<section class="pricing-section">
		<div class="section-header">
			<h2 class="section-title">Choose Your Path</h2>
			<p class="section-subtitle">Start free. Upgrade when you're ready to master more.</p>
		</div>

		<div class="pricing-grid">
			{#each pricingPlans as plan, i}
				<div
					class="pricing-card"
					class:highlighted={plan.highlighted}
					style="animation-delay: {i * 0.15}s"
				>
					{#if plan.highlighted}
						<div class="popular-badge">Most Popular</div>
					{/if}
					<h3 class="plan-name">{plan.name}</h3>
					<div class="plan-price">
						<span class="price">{plan.price}</span>
						<span class="period">{plan.period}</span>
					</div>
					<ul class="plan-features">
						{#each plan.features as feature}
							<li>
								<svg
									class="checkmark"
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="3"
									stroke-linecap="round"
									stroke-linejoin="round"
								>
									<polyline points="20 6 9 17 4 12"></polyline>
								</svg>
								{feature}
							</li>
						{/each}
					</ul>
					<button class="btn {plan.highlighted ? 'btn-primary' : 'btn-outline'} w-full">
						{plan.cta}
					</button>
				</div>
			{/each}
		</div>
	</section>

	<!-- CTA Section -->
	<section class="cta-section">
		<div class="cta-content">
			<h2 class="cta-title">Begin Your Language Journey Today</h2>
			<p class="cta-subtitle">
				Join thousands of learners discovering the joy of reading in a new language.
			</p>
			<button class="btn btn-primary btn-large">Start Reading Free</button>
			<p class="cta-note">No credit card required • 3 books free forever</p>
		</div>
	</section>

	<!-- Footer -->
	<footer class="footer">
		<div class="footer-content">
			<div class="footer-brand">
				<h3 class="footer-logo">readablock</h3>
				<p class="footer-tagline">Language immersion through literature</p>
			</div>
			<div class="footer-links">
				<div class="footer-column">
					<h4>Product</h4>
					<a href="#features">Features</a>
					<a href="#pricing">Pricing</a>
					<a href="#languages">Languages</a>
				</div>
				<div class="footer-column">
					<h4>Resources</h4>
					<a href="#github">GitHub</a>
					<a href="#guides">Learning Guides</a>
					<a href="#research">Research</a>
					<a href="#faq">FAQ</a>
				</div>
				<div class="footer-column">
					<h4>Company</h4>
					<a href="#about">About</a>
					<a href="#contact">Contact</a>
					<a href="#privacy">Privacy</a>
					<a href="#terms">Terms</a>
				</div>
			</div>
		</div>
		<div class="footer-bottom">
			<p>&copy; 2026 readablock. All rights reserved.</p>
		</div>
	</footer>
</div>

<style>
	:root {
		--bg-primary: #0a0a0a;
		--bg-secondary: #141414;
		--bg-tertiary: #1a1a1a;
		--text-primary: #e5e5e5;
		--text-secondary: #a3a3a3;
		--text-muted: #737373;
		--accent-primary: #d97706;
		--accent-secondary: #f59e0b;
		--border-color: #262626;
		--border-thick: 4px;
		--spacing-section: 10rem;
		--font-serif: 'Crimson Text', 'Georgia', serif;
		--font-display: 'Libre Baskerville', 'Georgia', serif;
	}

	:global(body) {
		margin: 0;
		padding: 0;
		background: var(--bg-primary);
		color: var(--text-primary);
		font-family: var(--font-serif);
		font-size: 18px;
		line-height: 1.7;
		overflow-x: hidden;
	}

	.app-container {
		width: 100%;
		min-height: 100vh;
	}

	/* Hero Section */
	.hero-section {
		min-height: 100vh;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 4rem 2rem;
		position: relative;
		border-bottom: var(--border-thick) solid var(--border-color);
	}

	.hero-content {
		max-width: 1400px;
		width: 100%;
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 6rem;
		align-items: center;
	}

	.hero-title {
		font-family: var(--font-display);
		font-size: clamp(3.5rem, 8vw, 7rem);
		font-weight: 700;
		line-height: 0.95;
		margin: 0 0 2rem 0;
		letter-spacing: -0.02em;
	}

	.gradient-text {
		background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		background-clip: text;
	}

	.hero-subtitle {
		font-size: 1.4rem;
		color: var(--text-secondary);
		margin: 0 0 3rem 0;
		max-width: 500px;
		line-height: 1.6;
	}

	.hero-cta {
		display: flex;
		gap: 1rem;
		flex-wrap: wrap;
	}

	/* Book Preview */
	.hero-demo {
		position: relative;
	}

	.book-preview {
		background: var(--bg-secondary);
		border: var(--border-thick) solid var(--border-color);
		border-radius: 8px;
		padding: 2rem;
		box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
		transform: perspective(1000px) rotateY(-5deg);
		transition: transform 0.3s ease;
	}

	.book-preview:hover {
		transform: perspective(1000px) rotateY(0deg);
	}

	.book-header {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding-bottom: 1.5rem;
		border-bottom: 2px solid var(--border-color);
		margin-bottom: 2rem;
	}

	.book-title {
		font-family: var(--font-display);
		font-size: 1.3rem;
		font-weight: 700;
		font-style: italic;
	}

	.book-progress {
		color: var(--text-muted);
		font-size: 0.9rem;
	}

	.book-content {
		position: relative;
		min-height: 300px;
	}

	.italian-text {
		font-size: 1.3rem;
		line-height: 2;
		margin: 0;
	}

	.word {
		background: none;
		border: none;
		color: var(--text-primary);
		font-family: inherit;
		font-size: inherit;
		cursor: pointer;
		padding: 2px 1px;
		transition: all 0.2s ease;
		position: relative;
		animation: fadeInWord 0.6s ease backwards;
	}

	@keyframes fadeInWord {
		from {
			opacity: 0;
			transform: translateY(10px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}

	.word:hover {
		color: var(--accent-secondary);
	}

	.word::after {
		content: '';
		position: absolute;
		bottom: 0;
		left: 0;
		right: 0;
		height: 2px;
		background: var(--accent-primary);
		transform: scaleX(0);
		transition: transform 0.2s ease;
	}

	.word:hover::after {
		transform: scaleX(1);
	}

	.word.selected {
		color: var(--accent-primary);
		font-weight: 600;
	}

	.translation-tooltip {
		position: absolute;
		bottom: 100%;
		left: 50%;
		transform: translateX(-50%);
		background: var(--bg-tertiary);
		border: 2px solid var(--accent-primary);
		padding: 1rem 1.5rem;
		border-radius: 8px;
		display: flex;
		flex-direction: column;
		gap: 0.5rem;
		animation: tooltipAppear 0.3s ease;
		box-shadow: 0 10px 30px rgba(0, 0, 0, 0.7);
	}

	@keyframes tooltipAppear {
		from {
			opacity: 0;
			transform: translateX(-50%) translateY(10px);
		}
		to {
			opacity: 1;
			transform: translateX(-50%) translateY(0);
		}
	}

	.tooltip-word {
		font-size: 1.2rem;
		font-weight: 700;
		color: var(--accent-secondary);
	}

	.tooltip-translation {
		font-size: 1rem;
		color: var(--text-secondary);
	}

	/* Scroll Indicator */
	.scroll-indicator {
		position: absolute;
		bottom: 3rem;
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 1rem;
		color: var(--text-muted);
		font-size: 0.9rem;
		letter-spacing: 0.1em;
		text-transform: uppercase;
	}

	.scroll-line {
		width: 2px;
		height: 60px;
		background: linear-gradient(to bottom, transparent, var(--border-color), transparent);
		animation: scrollPulse 2s ease-in-out infinite;
	}

	@keyframes scrollPulse {
		0%,
		100% {
			opacity: 0.3;
			transform: scaleY(1);
		}
		50% {
			opacity: 1;
			transform: scaleY(1.2);
		}
	}

	/* Features Section */
	.features-section {
		padding: var(--spacing-section) 2rem;
		border-bottom: var(--border-thick) solid var(--border-color);
	}

	.section-header {
		text-align: center;
		max-width: 800px;
		margin: 0 auto 6rem auto;
	}

	.section-title {
		font-family: var(--font-display);
		font-size: clamp(2.5rem, 5vw, 4rem);
		font-weight: 700;
		margin: 0 0 1.5rem 0;
		line-height: 1.1;
	}

	.section-subtitle {
		font-size: 1.3rem;
		color: var(--text-secondary);
		margin: 0;
	}

	.features-grid {
		max-width: 1400px;
		margin: 0 auto;
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
		gap: 3rem;
	}

	.feature-card {
		background: var(--bg-secondary);
		border: var(--border-thick) solid var(--border-color);
		padding: 3rem;
		position: relative;
		transition: all 0.3s ease;
		animation: fadeInUp 0.8s ease backwards;
	}

	@keyframes fadeInUp {
		from {
			opacity: 0;
			transform: translateY(40px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}

	.feature-card:hover {
		transform: translateY(-10px);
		border-color: var(--accent-primary);
	}

	.feature-card:hover .feature-border {
		transform: scaleX(1);
	}

	.feature-icon {
		font-size: 3.5rem;
		margin-bottom: 2rem;
		display: block;
	}

	.feature-title {
		font-family: var(--font-display);
		font-size: 1.8rem;
		font-weight: 700;
		margin: 0 0 1rem 0;
	}

	.feature-description {
		color: var(--text-secondary);
		margin: 0;
		font-size: 1.1rem;
	}

	.feature-border {
		position: absolute;
		bottom: 0;
		left: 0;
		right: 0;
		height: 4px;
		background: var(--accent-primary);
		transform: scaleX(0);
		transform-origin: left;
		transition: transform 0.3s ease;
	}

	/* How It Works Section */
	.how-section {
		padding: var(--spacing-section) 2rem;
		background: var(--bg-secondary);
		border-bottom: var(--border-thick) solid var(--border-color);
	}

	.how-content {
		max-width: 1400px;
		margin: 0 auto;
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 6rem;
		align-items: start;
	}

	.how-title {
		font-family: var(--font-display);
		font-size: clamp(2.5rem, 5vw, 4.5rem);
		font-weight: 700;
		line-height: 1;
		margin: 0 0 2rem 0;
	}

	.how-description {
		font-size: 1.3rem;
		color: var(--text-secondary);
		margin: 0 0 4rem 0;
		line-height: 1.7;
	}

	.how-stats {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 2rem;
	}

	.stat {
		border-left: var(--border-thick) solid var(--accent-primary);
		padding-left: 1.5rem;
	}

	.stat-number {
		font-family: var(--font-display);
		font-size: 3rem;
		font-weight: 700;
		line-height: 1;
		margin-bottom: 0.5rem;
		color: var(--accent-secondary);
	}

	.stat-label {
		font-size: 0.95rem;
		color: var(--text-muted);
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.process-steps {
		display: flex;
		flex-direction: column;
		gap: 3rem;
	}

	.process-step {
		display: grid;
		grid-template-columns: auto 1fr;
		gap: 2rem;
		align-items: start;
	}

	.step-number {
		font-family: var(--font-display);
		font-size: 4rem;
		font-weight: 700;
		line-height: 1;
		color: var(--text-muted);
	}

	.step-content h4 {
		font-family: var(--font-display);
		font-size: 1.6rem;
		font-weight: 700;
		margin: 0 0 0.75rem 0;
	}

	.step-content p {
		color: var(--text-secondary);
		margin: 0;
		font-size: 1.1rem;
	}

	/* Pricing Section */
	.pricing-section {
		padding: var(--spacing-section) 2rem;
		border-bottom: var(--border-thick) solid var(--border-color);
	}

	.pricing-grid {
		max-width: 1400px;
		margin: 0 auto;
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
		gap: 2rem;
	}

	.pricing-card {
		background: var(--bg-secondary);
		border: var(--border-thick) solid var(--border-color);
		padding: 3rem;
		position: relative;
		transition: all 0.3s ease;
		animation: fadeInUp 0.8s ease backwards;
	}

	.pricing-card.highlighted {
		border-color: var(--accent-primary);
		background: var(--bg-tertiary);
		transform: scale(1.05);
	}

	.pricing-card:hover {
		transform: translateY(-10px);
	}

	.pricing-card.highlighted:hover {
		transform: translateY(-10px) scale(1.05);
	}

	.popular-badge {
		position: absolute;
		top: -12px;
		left: 50%;
		transform: translateX(-50%);
		background: var(--accent-primary);
		color: var(--bg-primary);
		padding: 0.5rem 1.5rem;
		font-size: 0.85rem;
		font-weight: 700;
		text-transform: uppercase;
		letter-spacing: 0.1em;
	}

	.plan-name {
		font-family: var(--font-display);
		font-size: 1.8rem;
		font-weight: 700;
		margin: 0 0 1.5rem 0;
	}

	.plan-price {
		display: flex;
		align-items: baseline;
		gap: 0.5rem;
		margin-bottom: 2rem;
		padding-bottom: 2rem;
		border-bottom: 2px solid var(--border-color);
	}

	.price {
		font-family: var(--font-display);
		font-size: 3.5rem;
		font-weight: 700;
		line-height: 1;
	}

	.period {
		color: var(--text-muted);
		font-size: 1.1rem;
	}

	.plan-features {
		list-style: none;
		padding: 0;
		margin: 0 0 2.5rem 0;
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.plan-features li {
		display: flex;
		align-items: center;
		gap: 0.75rem;
		font-size: 1.05rem;
		color: var(--text-secondary);
	}

	.checkmark {
		width: 20px;
		height: 20px;
		color: var(--accent-primary);
		flex-shrink: 0;
	}

	/* CTA Section */
	.cta-section {
		padding: var(--spacing-section) 2rem;
		background: linear-gradient(135deg, var(--bg-primary), var(--bg-secondary));
		border-bottom: var(--border-thick) solid var(--border-color);
	}

	.cta-content {
		max-width: 800px;
		margin: 0 auto;
		text-align: center;
	}

	.cta-title {
		font-family: var(--font-display);
		font-size: clamp(2.5rem, 5vw, 4rem);
		font-weight: 700;
		margin: 0 0 1.5rem 0;
		line-height: 1.2;
	}

	.cta-subtitle {
		font-size: 1.4rem;
		color: var(--text-secondary);
		margin: 0 0 3rem 0;
	}

	.cta-note {
		margin-top: 1.5rem;
		color: var(--text-muted);
		font-size: 0.95rem;
	}

	/* Footer */
	.footer {
		padding: 6rem 2rem 3rem 2rem;
		background: var(--bg-secondary);
	}

	.footer-content {
		max-width: 1400px;
		margin: 0 auto;
		display: grid;
		grid-template-columns: 1.5fr 2fr;
		gap: 6rem;
		padding-bottom: 4rem;
		border-bottom: 2px solid var(--border-color);
	}

	.footer-logo {
		font-family: var(--font-display);
		font-size: 2rem;
		font-weight: 700;
		margin: 0 0 1rem 0;
	}

	.footer-tagline {
		color: var(--text-muted);
		margin: 0;
		font-size: 1.05rem;
	}

	.footer-links {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 3rem;
	}

	.footer-column h4 {
		font-family: var(--font-display);
		font-size: 1.1rem;
		font-weight: 700;
		margin: 0 0 1.5rem 0;
	}

	.footer-column a {
		display: block;
		color: var(--text-secondary);
		text-decoration: none;
		margin-bottom: 0.75rem;
		transition: color 0.2s ease;
		font-size: 1rem;
	}

	.footer-column a:hover {
		color: var(--accent-primary);
	}

	.footer-bottom {
		max-width: 1400px;
		margin: 0 auto;
		padding-top: 3rem;
		text-align: center;
		color: var(--text-muted);
		font-size: 0.95rem;
	}

	/* Buttons */
	.btn {
		font-family: var(--font-serif);
		font-size: 1.05rem;
		font-weight: 600;
		padding: 1rem 2.5rem;
		border: 2px solid transparent;
		cursor: pointer;
		transition: all 0.3s ease;
		text-transform: none;
		letter-spacing: 0.02em;
	}

	.btn-primary {
		background: var(--accent-primary);
		color: var(--bg-primary);
		border-color: var(--accent-primary);
	}

	.btn-primary:hover {
		background: var(--accent-secondary);
		border-color: var(--accent-secondary);
		transform: translateY(-2px);
		box-shadow: 0 10px 30px rgba(217, 119, 6, 0.3);
	}

	.btn-outline {
		background: transparent;
		color: var(--text-primary);
		border-color: var(--border-color);
	}

	.btn-outline:hover {
		border-color: var(--accent-primary);
		color: var(--accent-primary);
	}

	.btn-large {
		font-size: 1.2rem;
		padding: 1.25rem 3rem;
	}

	.w-full {
		width: 100%;
	}

	/* Responsive */
	@media (max-width: 1024px) {
		.hero-content,
		.how-content {
			grid-template-columns: 1fr;
			gap: 4rem;
		}

		.book-preview {
			transform: none;
		}

		.footer-content {
			grid-template-columns: 1fr;
			gap: 4rem;
		}

		.how-stats {
			grid-template-columns: repeat(3, 1fr);
		}
	}

	@media (max-width: 768px) {
		:root {
			--spacing-section: 6rem;
		}

		.hero-section {
			min-height: auto;
			padding: 6rem 1.5rem 4rem 1.5rem;
		}

		.hero-cta {
			flex-direction: column;
			width: 100%;
		}

		.hero-cta .btn {
			width: 100%;
			justify-content: center;
		}

		.features-grid,
		.pricing-grid {
			grid-template-columns: 1fr;
		}

		.how-stats {
			grid-template-columns: 1fr;
		}

		.footer-links {
			grid-template-columns: 1fr;
			gap: 2rem;
		}

		.italian-text {
			font-size: 1.1rem;
		}

		.pricing-card.highlighted {
			transform: scale(1);
		}

		.pricing-card.highlighted:hover {
			transform: translateY(-10px) scale(1);
		}
	}
</style>
