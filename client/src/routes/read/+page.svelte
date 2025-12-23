<script>
	import { onMount } from 'svelte';

	const baseURL = 'http://127.0.0.1:8000';

	let sentences = [];
	let sentenceLastRead = 0;

	async function getSentences() {
		const response = await fetch(`${baseURL}/app/read/`, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				sentence_last_read: sentenceLastRead
			})
		});
		const data = await response.json();

		sentences = data.sentences;
		sentenceLastRead = data.sentence_last_read;
	}

	onMount(async () => {
		await getSentences();

		const splitWords = (sentence) => {
			return sentence.split(/(\s+)/);
		};

		const handleWordClick = (word) => {
			alert(`You clicked: "${word}"`);
		};

		const handleTranslate = (sentence) => {
			alert(`Translate: "${sentence}"`);
		};
	});
</script>

<div class="min-h-screen bg-base-100 text-base-content">
	<div class="overflow-x-auto">
		<table class="table w-full border-collapse">
			<tbody>
				{#each sentences as sentence, index}
					<tr>
						<td class="border border-base-300 px-2 py-0">
							{#each splitWords(sentence) as part}
								{#if part.trim().length > 0}
									<button
										class="btn btn-ghost btn-xs normal-case p-0 m-0.5 hover:bg-base-300"
										on:click={() => handleWordClick(part)}
									>
										{part}
									</button>
								{:else}
									{part}
								{/if}
							{/each}
						</td>
						<td class="border border-base-300">
							<button on:click={() => handleTranslate(sentence)}> ⬇️ </button>
						</td>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</div>
